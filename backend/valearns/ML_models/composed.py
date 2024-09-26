import openai
import requests
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import json
from valearns.gpt_services import get_gpt_response
from valearns.google_search_services import FactCheckDataFetching
from bs4 import BeautifulSoup

# Preprocessing tools
nltk.download("punkt")
nltk.download("wordnet")
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# GPT-4 API key
openai.api_key = "your-openai-api-key"

# Bing Search API key and endpoint
bing_api_key = "your-bing-api-key"
bing_endpoint = "https://api.bing.microsoft.com/v7.0/search"

# Sample data to train the classifier
train_data = [
    ("What is quantum mechanics?", 0),  # 0 -> General chat, use GPT-4
    ("Latest AI news", 1),  # 1 -> Web search required
    ("How does the blockchain work?", 0),
    ("Weather in New York today", 1),
    ("Can you explain the big bang theory?", 0),
    ("Who won the football match yesterday?", 1),
    ("How much time does it take a baniyan tree to grow 20ft tall", 0),
]

# Preprocessing: Tokenization and Lemmatization
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    return " ".join(tokens)


# Preprocess training data
train_x = [preprocess_text(text) for text, label in train_data]
train_y = [label for text, label in train_data]

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer()
train_x_vectors = vectorizer.fit_transform(train_x)

# Train a simple classifier
classifier = DecisionTreeClassifier()
classifier.fit(train_x_vectors, train_y)


# Function to decide whether to use GPT-4 or a web search
def classify_query(query):
    query = preprocess_text(query)
    query_vector = vectorizer.transform([query])
    prediction = classifier.predict(query_vector)
    print(f"Prediction: {prediction}")
    return prediction[0]


# Function to call GPT-4 API
def call_gpt4(query):
    try:
        response = get_gpt_response(query)
        return response
    except Exception as e:
        return f"Error in GPT-4 API call: {str(e)}"


# Function to call Bing Web Search API
def perform_web_search(query):
    headers = {"Ocp-Apim-Subscription-Key": bing_api_key}
    params = {"q": query, "count": 1}

    try:
        response = requests.get(bing_endpoint, headers=headers, params=params)
        search_results = response.json()
        first_result = search_results["webPages"]["value"][0]
        title = first_result["name"]
        snippet = first_result["snippet"]
        url = first_result["url"]
        return f"{title}: {snippet}\nMore info: {url}"
    except Exception as e:
        return f"Error in web search: {str(e)}"


# Main function to handle user queries
def handle_query(query):
    # Classify the query: 0 -> GPT-4, 1 -> Web search
    if classify_query(query) == 0:
        # General chat, use GPT-4
        response = get_gpt_response(query)
        print("GPT-4 Response:")
        print(response)
    else:
        # Web search needed
        response = FactCheckDataFetching(query)
        print("Web Search Result:")
        print(response)


# Sample interaction
# while True:
#     user_query = input("Ask something: ")
#     if user_query.lower() == "exit":
#         break
#     handle_query(user_query)
