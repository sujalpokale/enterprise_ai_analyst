from rag.loader import load_all_pdfs
from rag.chunker import chunk_documents


documents = load_all_pdfs("documents")

chunks = chunk_documents(documents)

print("Documents:", len(documents))
print("Chunks:", len(chunks))

print(chunks[0].page_content)