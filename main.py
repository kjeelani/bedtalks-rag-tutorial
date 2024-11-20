import os
from openai import OpenAI
from dotenv import load_dotenv

from db.search import search_talks

load_dotenv()  # Load environment vars

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


REWRITE_TO_TITLE_PROMPT = """
Your job is to write the user query into a motivational video titles (5-8 words).
If the query seems hard to rewrite, just return "xxx"

Query: How can I stay motivated during tough times?
Title: Staying Motivated Through Life's Challenges

Query: What are some tips to be more productive?
Title: Mastering Productivity with Simple Strategies

Query: How do I build resilience in my life?
Title: Building Resilience to Overcome Life's Obstacles

Query: What’s the secret to being a good leader?
Title: The Key to Inspirational Leadership

Query: Krunchy Krispy Treats Eat My Feet
Title: xxx

Now rewrite the user query into a motivational video title:
"""

# Main Search Loop
while True:
    query = input("Enter your search query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break

    # Use the LLM to rewrite the query to a video title (give it System Prompt then User Query)
    rewritten_query = (
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": [{"type": "text", "text": REWRITE_TO_TITLE_PROMPT}],
                },
                {"role": "user", "content": [{"type": "text", "text": query}]},
            ],
            temperature=0.3,
        )
        .choices[0]
        .message.content
    )

    # Generate embedding for video title
    query_embedding = (
        client.embeddings.create(input=rewritten_query, model="text-embedding-3-small")
        .data[0]
        .embedding
    )

    # Search Pinecone for results -> in form {video_url, video_title}
    results = search_talks(query_embedding)

    # Display results
    print("\nTop Results:")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['url']}\n")
