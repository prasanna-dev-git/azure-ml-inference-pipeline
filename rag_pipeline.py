from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

# Load FAISS vector store
db = FAISS.load_local("vector_store", OpenAIEmbeddings())

# Initialize LLM
llm = OpenAI(temperature=0)

# Build Retrieval-Augmented QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Sample query
query = "What are the symptoms of diabetes?"
result = qa_chain.run(query)
print(f"Answer: {result}")
