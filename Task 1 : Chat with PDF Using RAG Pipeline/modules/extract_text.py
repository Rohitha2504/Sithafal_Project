import fitz  # PyMuPDF
from nltk import sent_tokenize
import nltk

nltk.download('punkt')

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text_data = {}
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_data[page_num + 1] = page.get_text("text")
    return text_data

def chunk_text(text, max_chunk_size=512):
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks
