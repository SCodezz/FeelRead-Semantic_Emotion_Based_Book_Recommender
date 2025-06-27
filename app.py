import pandas as pd
import numpy as np
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import gradio as gr

load_dotenv()

# Load dataset
books = pd.read_csv("books.csv")
books["description"] = books["description"].fillna("")

# Generate thumbnails if missing
books["large_thumbnail"] = books["thumbnail"].fillna("") + "&fife=w800"
books["large_thumbnail"] = np.where(
    books["large_thumbnail"] == "&fife=w800",
    "cover-not-found.jpg",
    books["large_thumbnail"],
)

# Create LangChain documents from book descriptions
documents = [
    Document(
        page_content=row["description"],
        metadata={"isbn": str(row["isbn13"])}
    )
    for _, row in books.iterrows()
]

# Initialize HuggingFace sentence transformer
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Vector store using ChromaDB
db_books = Chroma.from_documents(
    documents=documents,
    embedding=embedding_function,
    persist_directory="chroma_db"
)

# ✅ FIXED categories dropdown
categories = ["All", "Fiction", "Non-Fiction", "Children Fiction", "Children Non-Fiction"]

# Emotion tones and optional emotion columns
tones = ["All", "Happy", "Surprising", "Angry", "Suspenseful", "Sad"]
tone_to_column = {
    "Happy": "joy",
    "Surprising": "surprise",
    "Angry": "anger",
    "Suspenseful": "fear",
    "Sad": "sadness"
}

# Main recommendation logic
def retrieve_semantic_recommendations(query, category="All", tone="All", initial_top_k=50, final_top_k=16):
    recs = db_books.similarity_search(query, k=initial_top_k)
    matched_isbns = [rec.metadata.get("isbn") for rec in recs]
    book_recs = books[books["isbn13"].astype(str).isin(matched_isbns)].copy()

    # Filter by category if selected
    if category != "All":
        book_recs = book_recs[
            book_recs["categories"].str.lower().str.contains(category.lower(), na=False)
        ]

    # Filter/sort by tone column if available
    if tone != "All":
        col = tone_to_column.get(tone)
        if col in book_recs.columns:
            book_recs = book_recs.sort_values(by=col, ascending=False)

    return book_recs.head(final_top_k)

# Format for Gradio gallery
def recommend_books(query, category, tone):
    recommendations = retrieve_semantic_recommendations(query, category, tone)
    results = []

    for _, row in recommendations.iterrows():
        desc = row["description"]
        truncated_desc = " ".join(desc.split()[:30]) + "..."

        authors = row["authors"].split(";")
        if len(authors) == 2:
            author_str = f"{authors[0]} and {authors[1]}"
        elif len(authors) > 2:
            author_str = f"{', '.join(authors[:-1])}, and {authors[-1]}"
        else:
            author_str = row["authors"]

        caption = f"{row['title']} by {author_str}: {truncated_desc}"
        results.append((row["large_thumbnail"], caption))

    return results

# Gradio UI
with gr.Blocks(theme=gr.themes.Glass()) as dashboard:
    gr.Markdown("# 📚 Semantic Book Recommender")

    with gr.Row():
        user_query = gr.Textbox(label="Describe the kind of book you want", placeholder="e.g., A story about forgiveness")
        category_dropdown = gr.Dropdown(choices=categories, label="Filter by Category", value="All")
        tone_dropdown = gr.Dropdown(choices=tones, label="Filter by Emotion Tone", value="All")
        submit_button = gr.Button("Find Recommendations")

    gr.Markdown("## Recommended Books")
    output = gr.Gallery(label="Results", columns=4, rows=2)

    submit_button.click(
        fn=recommend_books,
        inputs=[user_query, category_dropdown, tone_dropdown],
        outputs=output
    )

if __name__ == "__main__":
    dashboard.launch()
