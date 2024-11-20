import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment vars
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# TODO: Fill in this prompt
REWRITE_TO_TITLE_PROMPT = """

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

    # TODO: Replace with proper function call
    results = []

    # Display results
    print("\nTop Results:")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['url']}\n")
