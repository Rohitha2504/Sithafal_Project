import numpy as np

def get_query_embedding(query):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode([query], convert_to_tensor=False)

def search_index(index, query_embedding, chunks, k=5):
    distances, indices = index.search(np.array(query_embedding), k)
    retrieved_chunks = [chunks[i] for i in indices[0]]
    return retrieved_chunks
