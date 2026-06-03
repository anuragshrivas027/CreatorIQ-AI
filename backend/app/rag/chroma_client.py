import chromadb

CHROMA_DB_PATH = "./chroma_db"

COLLECTION_NAME = (
    "video_transcripts"
)

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH
)

collection = (
    client.get_or_create_collection(
        name=COLLECTION_NAME
    )
)