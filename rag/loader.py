from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_all_pdfs(folder_path: str):
    
    doucments = []
    pdf_files = Path(folder_path).glob("*.pdf")
    
    for pdf_file in pdf_files:
        loader = PyPDFLoader(str(pdf_file))
        document = loader.load()
        doucments.extend(document)
    
    return doucments