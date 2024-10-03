from typing import Any
from django.core.management.base import BaseCommand
from valearns.train_model import model, vectorizer, train_y, train_x
import joblib


class Command(BaseCommand):
    help = "Pre Processing Function"

    def handle(self, *args: Any, **options: Any) -> str | None:
        X_vectorized = vectorizer.fit_transform(train_x)
        model.fit(X_vectorized, train_y)

        # Save the model and vectorizer
        joblib.dump(
            model, "./valearns/ml_models_data/model.pkl"
        )  # Save the trained model
        joblib.dump(
            vectorizer, "./valearns/ml_models_data/vectorizer.pkl"
        )  # Save the vectorizer
