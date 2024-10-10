import os
import asyncio
from langchain_core.tools import Tool
from django.conf import settings
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_community.document_loaders import AsyncChromiumLoader, AsyncHtmlLoader
from langchain_community.document_transformers import (
    BeautifulSoupTransformer,
    Html2TextTransformer,
)
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


os.environ["GOOGLE_CSE_ID"] = settings.GOOGLE_CSE_ID
os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
)

search = GoogleSearchAPIWrapper()

# Returns Compound Result
main_search_tool = Tool(
    name="google_main_search", description="Main concatenated search", func=search.run
)


def top_three(query):
    return search.results(query, 1)


# Returns relevant urls
url_fetching_tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=top_three,
)


def FactCheckDataFetching(query):
    compound_result = main_search_tool.invoke(query)

    return f"Result: {compound_result}"
