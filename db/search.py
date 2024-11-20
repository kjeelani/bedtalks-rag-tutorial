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

    # Get matches and filter them using the threshold
    raw_results = index.query(
        vector=query_embedding, top_k=max_res, include_metadata=True
    )
    filtered_results = [
        match["metadata"]
        for match in raw_results["matches"]
        if match["score"] >= threshold
    ]
    return filtered_results
