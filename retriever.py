from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

def call_api(query, options, context):
    load_dotenv()
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_db = Chroma(
        persist_directory="./twenty-thousand-leagues-under-the-sea-chroma_db", 
        embedding_function=embeddings_model
    )
    documents = vector_db.similarity_search(query)
    output = "\n".join(f'twenty-thousand-leagues-under-the-sea: {doc.page_content}' for doc in documents)

    result = {
        "output": output,
    }

    return result