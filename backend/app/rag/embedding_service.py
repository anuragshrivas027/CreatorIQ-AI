from sentence_transformers import (
    SentenceTransformer
)

MODEL_NAME = (
    "all-MiniLM-L6-v2"
)

model = SentenceTransformer(
    MODEL_NAME
)


def create_embedding(text):

    if not text:

        text = ""

    try:

        embedding = model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    except Exception as e:

        print(
            f"Embedding Error: {e}"
        )

        return [0.0] * 384