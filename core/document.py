from langchain.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk(file_path):
    loader = TextLoader(file_path)
    doc = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.create_documents([doc])
