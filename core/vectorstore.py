import os
import pinecone
from langchain_pinecone import PineconeVectorStore
from core.embeddings import get_embeddings

def get_vectorstore():
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )
    embeddings = get_embeddings()
    return PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX"),
        embedding=embeddings,
    )
