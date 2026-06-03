from rag.chroma_client import (
    collection
)

from rag.embedding_service import (
    create_embedding
)


def store_chunks(
    chunks,
    metadata
):

    video_id = metadata.get(
        "video_id"
    )

    if not video_id:
        return

    for index, chunk in enumerate(
        chunks
    ):

        try:

            embedding = create_embedding(
                chunk
            )

            collection.add(
                ids=[
                    f"{video_id}_{index}"
                ],
                embeddings=[
                    embedding
                ],
                documents=[
                    chunk
                ],
                metadatas=[
                    {
                        "video_id": metadata.get(
                            "video_id"
                        ),
                        "chunk_index": index,
                        "title": metadata.get(
                            "title"
                        ),
                        "creator": metadata.get(
                            "creator"
                        ),
                        "views": metadata.get(
                            "views"
                        ),
                        "likes": metadata.get(
                            "likes"
                        ),
                        "comments": metadata.get(
                            "comments"
                        ),
                        "engagement_rate": metadata.get(
                            "engagement_rate"
                        )
                    }
                ]
            )

        except Exception as e:

            print(
                f"Chunk Storage Error: {e}"
            )


def search_chunks(
    query,
    top_k=5
):

    try:

        query_embedding = (
            create_embedding(
                query
            )
        )

        results = collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=top_k
        )

        return results

    except Exception as e:

        print(
            f"Vector Search Error: {e}"
        )

        return {
            "documents": [[]],
            "metadatas": [[]]
        }