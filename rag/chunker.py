from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import settings

def chunk_documents(documents):
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )
    
    chunks = splitter.split_documents(documents)
    
    return chunks
