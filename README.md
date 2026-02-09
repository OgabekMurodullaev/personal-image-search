# Personal Image Search Engine

🚀 **Overview**  
This project is a **personal image search engine** built using **Weaviate** and **ResNet50 embeddings**.  
It allows users to upload an image and retrieve the **top-3 most similar images** from a custom image collection.  
Additionally, the project explores **Retrieval-Augmented Generation (RAG)** techniques for semantic search and future multimodal queries.

---

## 🔹 Features

- Index 100+ images using ResNet50 embeddings
- Similarity search with high accuracy
- **Streamlit UI** to upload images and instantly view top-3 similar results
- Displays **distance** and **certainty** for each result
- Easy to extend with RAG for semantic queries

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Weaviate** (vector database)
- **PIL / Pillow** (image processing)
- **Streamlit** (UI)
- **ResNet50** pretrained model for embeddings

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/ogabekmurodullaev/personal-image-search.git
cd personal-image-search```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt```

3. Run Weaviate using Docker:
```bash
docker-compose up -d
```

4. Prepare and index images:
``` bash
python utils.py        # Convert images to JPG, resize to 224x224
python indexer.py      # Insert images into Weaviate 
```
🚀 Run the Streamlit UI
```bash
streamlit run main.py
```

📌 Author

Ogabek Murodullayev
