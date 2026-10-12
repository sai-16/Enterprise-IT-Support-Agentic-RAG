# from app.core.config import get_settings

# settings = get_settings()

# print(f"App Name: {settings.app_name}")
# print(f"App Environment: {settings.app_env}")


# from app.services.ingestion import load_file, chunk_documents

# from pathlib import Path
# from app.rag.vectorstore import add_documents

# docs = load_file(Path("data/sample_kb/company_it_handbook.md"))

# chucks = chunk_documents(docs)

# add_documents(chunks)

# print(f"Loaded and chunked {len(docs)} documents.")


import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)