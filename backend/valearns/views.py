from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from valearns.gpt_services import (
    get_gpt_response,
    tokenLimit,
    get_gpt_response_with_context,
)
from valearns.ML_models.preprocessing import preprocess_input
from valearns.ML_models.Classifier import classify_input
from valearns.ML_models.model import load_model, load_vectorizer
from valearns.train_model import update_model, train_initial_model
from valearns.google_search_services import FactCheckDataFetching
from valearns.scrapping import scrape_webpage
from valearns.scrapping import similaritySearch
from openai import APIConnectionError, RateLimitError, OpenAIError
import json
import openai

# Load pre-trained ML model and vectorizer
model = load_model(
    "./valearns/ml_models_data/model.pkl"
)  # Replace with your actual model filename
vectorizer = load_vectorizer(
    "./valearns/ml_models_data/vectorizer.pkl"
)  # Replace with your actual vectorizer filename


@csrf_exempt  # Use this only if you want to disable CSRF protection for testing purposes
def chatbot_view(request):
    if request.method == "POST":
        try:
            # Ensure the request body is in JSON format
            data = json.loads(request.body.decode("utf-8"))
            user_input = data.get("user_input")

            if user_input is None:
                return JsonResponse(
                    {"error": "Missing 'user_input' in request."}, status=400
                )

            # Preprocess input
            cleaned_input = preprocess_input(user_input)

            # Classify user intent using the cleaned input
            intent = classify_input(cleaned_input, vectorizer, model)

            update_model(user_input, intent)

            user_input_token_count = tokenLimit(user_input)

            if user_input_token_count:
                # Based on intent, either respond with GPT or a predefined response
                if intent == "LLM":
                    try:
                        response_text = get_gpt_response(user_input)
                    except openai.APIConnectionError:
                        return JsonResponse(
                            {"error": "api-connection-error/@openai"},
                            status=503,  # This 503 status code indicates service unavailable
                        )
                    except openai.RateLimitError:
                        return JsonResponse(
                            {"error": "rate-limit-error/@openai"}, status=503
                        )
                    except openai.OpenAIError:
                        return JsonResponse(
                            {"error": "open-ai-error/@openai"}, status=503
                        )
                elif intent == "Internet Search":
                    response_text = ""
                    try:
                        response_text = FactCheckDataFetching(user_input)
                        response_text = get_gpt_response_with_context(
                            response_text, user_input
                        )
                    except Exception as e:
                        return e
                else:
                    response_text = similaritySearch(user_input)
                    response_text = get_gpt_response_with_context(
                        response_text, user_input
                    )
                # Return a JSON response
                return JsonResponse({"response": response_text})
            else:
                # Returns if the input limit exists the maximum Amount
                return JsonResponse({"error": "Token Limit Error"}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    # Return a JSON response for non-POST requests
    return JsonResponse({"error": "Invalid request method."}, status=400)
