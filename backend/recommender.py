import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset once
with open("data/places.json", "r", encoding="utf-8") as f:
    PLACES_DB = json.load(f)


def build_city_index(city):
    """
    Builds FAISS index for a specific city.
    """
    places = PLACES_DB.get(city.title(), [])
    if not places:
        return None, []

    descriptions = [p["description"] + " " + p["name"] for p in places]
    embeddings = model.encode(descriptions)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    return index, places


def recommend_places(city, query_text, top_k=5):
    """
    Returns the top-k most relevant places for a given query.
    """
    index, places = build_city_index(city)

    if index is None or not places:
        return []

    query_emb = model.encode([query_text])
    D, I = index.search(np.array(query_emb).astype("float32"), top_k)

    results = [places[i] for i in I[0]]
    return results
