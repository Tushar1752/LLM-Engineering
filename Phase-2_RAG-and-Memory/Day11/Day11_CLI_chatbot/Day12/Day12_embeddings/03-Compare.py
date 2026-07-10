""" Similar vs different -- ranking by MEANING, not keywords.
We embed a query and a few documents, then score each doc against the query
with cosine similarity (higher = more alike). The "automobile" sentence ranks
near the top for "motor vehicle" even though they share NO words -- proof that
embeddings match meaning, not letters.
Setup: pip install sentence-transformers numpy

"""

from sentence_transformers import SentenceTransformer, util

DOCS = [
    "A car is a four-wheeled vehicle for the road",
    "An automobile takes you from place to place",     # 'car' meaning, different words
    "The chef cooked a delicious pasta dinner",
    "Photosynthesis lets plants make food from light",
]
QUERY ="How does a motor vehicle work?"

def main():

    # Embed the query and all docs.

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec= model.encode(QUERY)
    docs_vec = model.encode(DOCS)
    # cos_sim returns a 1 x len(DOCS) matrix; [0] grabs the single row of scores.

    scores=util.cos_sim(query_vec,docs_vec)[0]
    print(scores)

if __name__ == "__main__":
    main()