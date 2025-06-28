




# 📚 FeelRead: Semantic & Emotion-Aware Book Recommender

An interactive book recommendation system that understands your emotions and query intent to suggest meaningful reads. FeelRead uses semantic search and emotion tone filtering to personalize book recommendations. Built using Hugging Face Transformers, ChromaDB, and Gradio.

🟢 **Live Demo**: [Try on Hugging Face](https://huggingface.co/spaces/Shreya-S1/feelread-semantic-emotion-book-recommender)

---

## 🚀 Features

- 🔍 **Semantic Search** – Understands natural language queries using sentence-transformer embeddings.
- 😊 **Emotion-Tone Filtering** – Filter results by emotions like Happy, Sad, Angry, Suspenseful, etc.
- 🧠 **Category Selection** – Choose from genres like Fiction, Non-Fiction, Children’s Fiction/Non-Fiction.
- 🖼️ **Visual Output** – Gallery-style recommendations with thumbnails, author names, and short descriptions.
- ⚡ **Fast Vector Retrieval** – Uses ChromaDB for efficient similarity search over book descriptions.

---

## 🛠️ Tech Stack

| Purpose        | Tool/Library                             |
|----------------|------------------------------------------|
| Embeddings     | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store   | ChromaDB                                 |
| UI             | Gradio (Blocks & Gallery)                |
| Text Handling  | LangChain, Pandas, NumPy                 |

---

## 📂 Folder Structure

```bash
FeelRead/
├── app.py               # Main Gradio app
├── books.csv            # Dataset of books with descriptions
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── .gitignore           # Files/folders to ignore in Git
└── LICENSE              # MIT License
````

---

## ⚙️ Setup & Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/SCodezz/FeelRead.git
cd FeelRead
```

### 2. Set up a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

➡️ Gradio will launch your app in the browser.

---

## 📈 Example Use Cases

* “Books about self-discovery with a happy tone.”
* “Children’s stories that are sad but inspiring.”
* “Suspenseful fiction about betrayal.”

---


## 👩‍💻 Author

**Shreya S**
Final Year B.Tech (CSE - Artificial Intelligence & Data Science)
[GitHub](https://github.com/SCodezz) • [Hugging Face Space](https://huggingface.co/spaces/Shreya-S1/feelread-semantic-emotion-book-recommender)

---

## ⚙️ Hugging Face Space Metadata

```yaml
---
title: 'FeelRead: Semantic & Emotion-Based Book Recommender'
emoji: 📉
colorFrom: blue
colorTo: blue
sdk: gradio
sdk_version: 5.34.2
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
```


