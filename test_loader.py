from rag.loader import load_all_pdfs

docs = load_all_pdfs("documents")

print("Total Pages:", len(docs))

print(docs[0].page_content[:300])

print(docs[0].metadata)