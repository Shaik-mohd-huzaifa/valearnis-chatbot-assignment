import numpy as np
from openai import AzureOpenAI
from django.conf import settings
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from django.conf import settings
import os
from langchain_openai import AzureOpenAIEmbeddings


AZURE_OPENAI_ENDPOINT = settings.AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_KEY = settings.AZURE_OPENAI_API_KEY
AZURE_OPENAI_API_VERSION = "2024-02-01"


# Change this with your OpenAIEmbeddings or Other
embeddingo = AzureOpenAIEmbeddings(
    model="text-embedding-3-small",
    chunk_size=250,
)

VECTOR_STORE_PATH = "./valearns/vectorStore"


# Web scraping function
def scrape_webpage():
    urls = [
        "https://valearnis.com/about-us",
        "https://valearnis.com/subjects",
        "https://valearnis.com/pricing",
        "https://valearnis.com/",
    ]
    loader = WebBaseLoader(urls)

    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=20)
    all_splits = text_splitter.split_documents(docs)

    return all_splits


def update_vectorStore():
    docs = scrape_webpage()

    vectorStore = FAISS.from_documents(docs, embeddingo)

    vectorStore.save_local(VECTOR_STORE_PATH)


# Scraped Data from webpages is converted into embeddings and stored in VectorStore
# update_vectorStore()


def similaritySearch(query):
    vectorStore = FAISS.load_local(
        VECTOR_STORE_PATH, embeddingo, allow_dangerous_deserialization=True
    )

    search_results = vectorStore.similarity_search_with_score(query)

    result_data = [
        {
            "similarity_score": float(score),  # Convert numpy.float32 to Python float
            "document_content": doc.page_content,
            "document_metadata": doc.metadata,
        }
        for doc, score in search_results
    ]

    result = ""

    for doc in result_data:
        result = result + "\n" + doc["document_content"]

    return result
