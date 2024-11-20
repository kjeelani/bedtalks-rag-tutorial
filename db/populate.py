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


# Create (if necessary) the indez and load it
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

    # Add to Pinecone DB
    index.upsert(
        [
            (
                bed_talk["video_url"],
                embedding,
                {"title": bed_talk["video_title"], "url": bed_talk["video_url"]},
            )  # (id, embedding, metadata to be retrieved)
        ]
    )
