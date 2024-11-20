# RAG Tutorial with BED Talks Example
The goal of this exercise is to familiarize yourself with programming using Python, OpenAI, and Vector Databases (namely Pinecone). The set up and the four introduction questions 
are simply meant to help you familiarize yourself with documentation and prompt engineering, but the rest of this lab will be more open-ended.

## BED (Better Every Day) Talks Introduction
BED Talks aims to deliver powerful motivational talks to audiences worldwide. However, their existing keyword-based search system falls short in enabling users to find niche or specific topics. This project tackles the challenge by implementing a Retrieval-Augmented Generation (RAG) system using an LLM for query rewriting and Pinecone for semantic search. The result? A smarter, more intuitive search experience.

## Getting Started
### **Clone the Repository**
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/kjeelani/bedtalks-rag-tutorial.git
cd bedtalks-rag-tutorial
```

### **Set up your Virtual Environment**
1) Open the folder in VSCode if not done already
2) In a terminal, enter `python -m venv env`. This sets up your virtual environment (more on that [here](https://docs.python.org/3/library/venv.html))
3) Then, if you are on Windows enter `env/Scripts/activate`. If you are on Mac enter `source env/bin/activate`. You should see in your terminal (env) before each line.
4) Finally enter `pip install pinecone-client openai python_dotenv`. You are now ready to work with the repository!

### **Set up a Pinecone Account**
To use Pinecone:
1) [Sign up here](https://www.pinecone.io/)
2) Generate a Pinecone API key on the left sidebar
3) Create a new Pinecone Index called `bed-talks`

### **Set up the Environment File**
1) Create a new file in the root repository called .env
2) Obtain the OpenAI key we will use [here](https://docs.google.com/document/d/1waHiWHV4K9xmzc44UEij-neAojGx9opUaHGDI4BKLfM/edit?usp=sharing). If you do not have access, let me know.
```
OPENAI_API_KEY=""
PINECONE_API_KEY=""
PINECONE_INDEX_NAME="bed-talks"
```

## Completing Introductory Tasks
To get the most minimal example running, complete the four TODOs in the repo
1) In `db/populate.py`, use the Pinecone documentation to understand how to upsert (insert with update) your embedding and associate it with metadata. Then fill out the TODO.
2) In `db/search.py`, use the Pinecone documentation to understand how to query your Pinecone database with your embedding. Then fill out the TODO.
3) In `main.py`, import the proper function to search the Pinecone database in the TODO within the loop
4) Finally, in `main.py` at the top, fill out the `REWRITE_TO_TITLE_PROMPT` with proper prompt engineering to convert any query into a title.

If you are stuck on any of these tasks, please refer to the solution branch of this project

## The Exploration Phase
This is already pretty useful as is, but how can we make this more interesting? Here are some possible directions you can take this project:
1) The most basic but powerful idea is to incorperate the transcript somehow within our embedding or to retrieve the transcript for a more nuanced and detailed search result. 
2) When we as users use ChatGPT, we can get better results by iterating on results. Can we create a similar system where we incorporate user feedback to iteratively refine the search results?
3) This system works great for 10 data points. But what about 1k? 1mil? Amazon shopping results use similar techniques but probably have 100+ million items in its shop. What techniques can we utilize for more efficient searching (Hint: look at sharding).
