from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import os

def build_qa_chain(vectorstore):
    llm = ChatOpenAI(
        model_name="gpt-4", 
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
