# your_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .gpt_services import get_gpt_response
from .ML_models.preprocessing import preprocess_input
from .ML_models.Classifier import classify_input
from .ML_models.model import load_model, load_vectorizer
from .ML_models.composed import handle_query
from .train_model import update_model
from valearns.google_search_services import FactCheckDataFetching
import json

# Load pre-trained ML model and vectorizer
model = load_model(
    "./valearns/ml_models_data/Model_V1.pkl"
)  # Replace with your actual model filename
vectorizer = load_vectorizer(
    "./valearns/ml_models_data/Vectorizer_V2.pkl"
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

            # Based on intent, either respond with GPT or a predefined response
            if intent == 0:
                response_text = get_gpt_response(user_input)
            else:
                response_text = FactCheckDataFetching(user_input)

            # Return a JSON response
            return JsonResponse({"response": response_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    # Return a JSON response for non-POST requests
    return JsonResponse({"error": "Invalid request method."}, status=400)


@csrf_exempt
def ask(request):
    if request.method == "POST":
        # Ensure the request body is in JSON format
        data = json.loads(request.body.decode("utf-8"))
        user_input = data.get("user_input")
        response = handle_query(user_input)
        return JsonResponse({"response": response})
