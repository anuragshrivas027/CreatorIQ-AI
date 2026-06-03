from rag.text_splitter import (
    split_text
)

from rag.vector_store import (
    store_chunks
)


def process_transcript(
    transcript,
    metadata
):

    if not transcript:

        return 0

    try:

        chunks = split_text(
            transcript
        )

        if not chunks:

            return 0

        store_chunks(
            chunks,
            metadata
        )

        return len(
            chunks
        )

    except Exception as e:

        print(
            f"Transcript Processing Error: {e}"
        )

        return 0