from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv() 
pdf_path = Path(__file__).parent / "David_seidi.pdf"

# loading file into python program 
loader = PyPDFLoader(file_path = pdf_path)
docs = loader.load()

# split the docs into smaller chunks 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)
chunks = text_splitter.split_documents(documents = docs)

# creating vector embeddings for this code 
embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

vectore_store = QdrantVectorStore.from_documents(
    documents = chunks, 
    embedding = embedding_model,
    url = "http://localhost:6333",
    collection_name = "learning_rag"
)
print("indexing of documents done ....")