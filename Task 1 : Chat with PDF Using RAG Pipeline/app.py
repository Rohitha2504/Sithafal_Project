from flask import Flask, request, render_template
from modules.extract_text import extract_text_from_pdf, chunk_text
from modules.embeddings import create_embeddings, store_embeddings
from modules.retriever import search_index, get_query_embedding
from modules.response_generator import generate_response
import pdfplumber
import pandas as pd


# Flask App
app = Flask(__name__)

# Load and preprocess data
pdf_text = extract_text_from_pdf(r"C:\Users\rohit\Downloads\Task 1 Chat with PDF Using RAG Pipeline\data\example.pdf")
chunks = [chunk_text(page_text) for page_text in pdf_text.values()]
all_chunks = [item for sublist in chunks for item in sublist]
embeddings = create_embeddings(all_chunks)
index, stored_chunks = store_embeddings(embeddings, all_chunks)

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]  # assuming the table is on the first page
        table = first_page.extract_table()
        return table

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        query = request.form["question"]
        query_embedding = get_query_embedding(query)
        relevant_chunks = search_index(index, query_embedding, stored_chunks)
        answer = generate_response(query, " ".join(relevant_chunks))
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)