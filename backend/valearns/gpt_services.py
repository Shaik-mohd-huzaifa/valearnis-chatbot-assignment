import tiktoken  # Use the tiktoken library for token counting

# your_app/gpt_services.py

from openai import AzureOpenAI
from langchain_core.prompts import PromptTemplate
import openai
from django.conf import settings

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    azure_deployment="wasp-ai",
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version="2023-05-15",
)


def get_gpt_response(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o",
        max_tokens=1000,
    )
    return response.choices[0].message.content


def tokenLimit(prompt):
    # Choose the encoding that matches your model
    encoding = tiktoken.encoding_for_model("gpt-4o")

    # Count the number of tokens
    token_count = len(encoding.encode(prompt))

    if token_count > 1081:
        return False
    else:
        return True


prompt_template = """
    You are a assisstant to answer the user queries based on the context provided. Respond with the context if the context is empty try to answer on your own
    
    Context: {context}
    
    Query: {query}
"""

prompt = PromptTemplate.from_template(template=prompt_template)


def get_gpt_response_with_context(prompt, query_context):
    formatted_prompt = prompt.format(context=query_context, query=prompt)

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": formatted_prompt}],
        model="gpt-4o",
        max_tokens=1000,
    )
    return response.choices[0].message.content
