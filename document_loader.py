import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# Load documents from folder
loader = DirectoryLoader("docs", glob="**/*.txt")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Embed and store in FAISS
embedding = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embedding)
db.save_local("vector_store")
print("Vector store created and saved.")
