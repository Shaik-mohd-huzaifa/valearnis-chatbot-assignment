import tiktoken  # Use the tiktoken library for token counting
from openai import AzureOpenAI, OpenAI
from langchain_core.prompts import PromptTemplate
import openai
from django.conf import settings

# Replace it with your Credentials
client = OpenAI(api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_ENDPOINT)

def get_gpt_response(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a Assistant who answer users queries. Response in normal text no markdown responses",
            },
            {"role": "user", "content": prompt},
        ],
        model="gpt-4o",
        max_tokens=1000,
    )
    return response.choices[0].message.content


def tokenLimit(prompt):
    # Choose the encoding that matches your model
    encoding = tiktoken.encoding_for_model("gpt-4o")

    # Count the number of tokens
    token_count = len(encoding.encode(prompt))

    if token_count > 10:
        return False
    else:
        return True


prompt_template = """
    You are a assisstant to answer the user queries based on the context provided. Respond with the context if the context is empty try to answer queries on your own and no markdown response only respond in normal text 
    Context: {context}
    
    Query: {query}
"""

prompt = PromptTemplate.from_template(template=prompt_template)

# GPT Service where the user query and context is passed for response
def get_gpt_response_with_context(prompt, query_context):
    formatted_prompt = prompt.format(context=query_context, query=prompt)

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": formatted_prompt}],
        model="gpt-4",
        max_tokens=1000,
    )
    return response.choices[0].message.content
