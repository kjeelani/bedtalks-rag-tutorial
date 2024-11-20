from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment vars

"""
    READ!!!
    
    You only need to run this once to populate your Pinecone Vector DB.
"""

# Initialize Pinecone and OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


# Create (if necessary) the index and load it
index_name = os.getenv("PINECONE_INDEX_NAME")
if index_name not in pinecone.list_indexes().names():
    pinecone.create_index(
        index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
index = pinecone.Index(index_name)


# Load BED Talks data
with open("bed_talks.json", "r") as file:
    bed_talks = json.load(file)


# Generate embeddings and upsert to Pinecone
for bed_talk in bed_talks:
    # Create embedding of video title
    embedding = (
        client.embeddings.create(
            input=bed_talk["video_title"], model="text-embedding-3-small"
        )
        .data[0]
        .embedding
    )

    """
        TODO: Determine how to add to the Pinecone Database using it's documentation

        You need to use the video_url as the id, pass in the embedding, and the metadata 
        
        Metadata should be in the following form:
        {
            video_url: str,
            video_title: str,
            speakers: str,
            video_transcript: str
        }
    """
