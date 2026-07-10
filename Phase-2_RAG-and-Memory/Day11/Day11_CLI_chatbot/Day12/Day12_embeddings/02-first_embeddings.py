"""
Day 17 - Step 2: Your first REAL embedding (local, free, no API key).

We load a small trained model (all-MiniLM-L6-v2) and turn text into a vector
of 384 numbers. Unlike module 01, we don't pick the numbers -- the model does,
from having read billions of sentences.

First run downloads the model (~90 MB) to a local cache, then it's offline.

Setup: pip install sentence-transformers numpy
Run:   python first_embedding.py
"""

from sentence_transformers import SentenceTransformer


def main():
    print("Loading model 'all-MiniLM-L6-v2' (first run downloads ~90 MB)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # --- one sentence -> one vector ---
    sentence = "I love learning about AI"
    vector = model.encode(sentence)
    print(vector)


if __name__ == "__main__":
    main()