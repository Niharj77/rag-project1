from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Step 1: Load PDF
loader = PyPDFLoader("data/devops.pdf")
documents = loader.load()

# Step 2: Create a text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Step 3: Split the documents into chunks
chunks = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

# Step 4: Print information
print(f"Total Pages: {len(documents)}")
print(f"Total Chunks: {len(chunks)}")

print("Embeddings created successfully!")
print("Vector database stored in chroma_db/")