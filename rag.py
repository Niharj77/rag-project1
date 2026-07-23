import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()

# Check if API key exists
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

# Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load the existing Chroma vector database
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# User query
query = "What is Docker?"

# Retrieve the top 3 relevant chunks
results = vector_db.similarity_search(query, k=3)

# Combine retrieved chunks into a single context string
context = "\n\n".join([doc.page_content for doc in results])

# Create the prompt
prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the context provided below.
If the answer is not available in the context, reply:
"I couldn't find that information in the provided document."

Context:
{context}

Question:
{query}

Answer:
"""

# Send the prompt to Gemini
response = llm.invoke(prompt)

# Print the final answer
print("\n========== FINAL ANSWER ==========\n")
print(response.content)