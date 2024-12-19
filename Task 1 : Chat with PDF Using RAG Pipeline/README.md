## Task 1 : Chat With PDF Using RAG Pipeline
### Retrieval-Augmented Generation (RAG) Pipeline

## Overview
The RAG pipeline project extracts, processes, and retrieves relevant information from semi-structured data sources like PDFs using a combination of natural language processing (NLP) models and vector-based retrieval systems. It answers user queries through a web interface by leveraging language models.

---

## Project Structure
```
rag-pipeline/
│
├── app.py                   # Main application file (Flask server)
├── requirements.txt         # File listing all dependencies for the project
│
├── data/                    # Directory to store PDF files
│   └── example.pdf          # Example PDF file for processing
│
├── modules/                 # Directory for modularized Python scripts
│   ├── extract_text.py      # Handles PDF text extraction and chunking
│   ├── embeddings.py        # Embedding generation and vector storage
│   ├── retriever.py         # Retrieval logic for similarity search
│   └── response_generator.py # Generates responses using LLMs
│
├── static/                  # Static files for the web app (CSS, JS, etc.)
│   └── styles.css           # Optional styles for the web interface
│
├── templates/               # HTML templates for Flask
│   └── index.html           # Web interface for user interaction
│
└── logs/                    # Directory for logs (optional)
    └── app.log              # Log file for debugging
```

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/rag-pipeline.git
   cd rag-pipeline
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the Web Interface:**
   Visit `http://localhost:5000` in your browser.

---

## How It Works

1. **Upload Data:** Upload PDF files into the `data/` directory.
2. **Query Submission:** Enter a query through the web interface.
3. **Text Extraction:** Extracts and processes the text from PDFs.
4. **Embeddings Generation:** Generates vector embeddings for text chunks.
5. **Information Retrieval:** Searches for relevant content using FAISS.
6. **Response Generation:** Uses an LLM to generate answers based on retrieved data.
7. **Display Results:** Presents results in a tabular or textual format on the web interface.

---

## Technologies Used

- **Backend:** Flask, PyTorch, Hugging Face Transformers
- **PDF Processing:** `pdfplumber`
- **Vector Search:** FAISS
- **Frontend:** HTML, CSS (Flask Templates)

---

## Contribution

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgments

- Hugging Face for pre-trained models.
- FAISS for efficient similarity search.

---

**Note:** Customize this README file with your own project details before uploading to GitHub.
