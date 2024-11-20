from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Pinecone and OpenAI
pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = os.getenv("PINECONE_INDEX_NAME")


def search_talks(query_embedding, max_res=3, threshold=0.4):
    """
    Given the query embedding, find up to max_res results
    that have a similarity score > threshold

    Output:
    {
        video_title: str,
        video_url: str,
        video_transcript: str
    }
    """

    # Attempt to load the index or log a warning and return nothing
    if index_name not in pinecone.list_indexes().names():
        print("WARNING: Index Not Loaded")
        return []
    index = pinecone.Index(index_name)

    results = []
    """
        TODO: Query the index and filter the metadata to ensure
        only results with similarity score above the threshold
        are returned.

        Also make sure to use the max_res parameter to limit search results
    """

    return results
