# your_app/gpt_services.py

from openai import AzureOpenAI
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
        model="gpt-4o-2024-05-13",
    )
    return response.choices[0].message.content
