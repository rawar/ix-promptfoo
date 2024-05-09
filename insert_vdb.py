import urllib.request
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain import hub
from dotenv import load_dotenv

url = 'https://www.gutenberg.org/cache/epub/164/pg164.txt'
filename = 'twenty-thousand-leagues-under-the-sea.txt'

urllib.request.urlretrieve(url, filename)

loader = TextLoader(filename)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(documents)

load_dotenv()
llm = OpenAI(temperature=0.1, model_name="gpt-3.5-turbo")
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

vector_db = Chroma.from_documents(
    documents=all_splits, 
    embedding=embeddings_model,
    persist_directory="./twenty-thousand-leagues-under-the-sea-chroma_db"
)




