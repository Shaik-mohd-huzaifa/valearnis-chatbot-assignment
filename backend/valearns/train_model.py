# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import joblib
from valearns.data.training_data import train_data


def train_initial_model():
    # Convert to DataFrame
    df = pd.DataFrame(train_data)

    # Split the dataset into features and labels
    train_x = [text for text, label in train_data]
    train_y = [label for text, label in train_data]

    # Create a TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(train_x)

    # Train a classifier (e.g., Decision Tree)
    model = DecisionTreeClassifier()
    model.fit(X_vectorized, train_y)

    # Save the model and vectorizer
    joblib.dump(model, "./valearns/ml_models_data/Model_V1.pkl")
    joblib.dump(vectorizer, "./valearns/ml_models_data/Vectorizer_V1.pkl")


# Function to update the model with new data
def update_model(new_query, new_label):
    # Load the pre-trained model and vectorizer
    model = joblib.load("./valearns/ml_models_data/Model_V1.pkl")
    vectorizer = joblib.load("./valearns/ml_models_data/Vectorizer_V1.pkl")
    # Vectorize the new query
    new_query_vectorized = vectorizer.transform([new_query])

    train_x = [text for text, label in train_data]
    train_y = [label for text, label in train_data]

    # Append the new data to the current dataset and retrain the model
    # You might need to store historical queries if you want to keep the old data
    train_x.append(new_query)
    train_y.append(new_label)

    # Retrain the model with the updated data
    X_vectorized = vectorizer.fit_transform(train_x)
    model.fit(X_vectorized, train_y)

    # Save the updated model and vectorizer
    joblib.dump(model, "./valearns/ml_models_data/Model_V1.pkl")
    joblib.dump(vectorizer, "./valearns/ml_models_data/Vectorizer_V2.pkl")
    print("New Query Updated")
