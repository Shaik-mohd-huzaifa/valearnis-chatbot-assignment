# ValeArnis Django Project

This project is a **Django-based backend** that integrates multiple Machine Learning (ML) services, scrapes web data, and interacts with OpenAI's Azure services. The primary functionality of this project includes text predictions using a trained ML model, and handling LLM, RAG (Retrieval-Augmented Generation), and Internet Search.

## Project Structure

```bash
backend/
│
├── backend/                    # Django settings and configuration folder
│   ├── __pycache__/
│   ├── settings.py             # Main Django settings file
│   ├── urls.py                 # Django URL routing
│   ├── wsgi.py                 # WSGI entry point for the project
│   └── .env                    # Environment variables file (added for API keys and other secrets)
│
├── valearns/                   # Main app folder
│   ├── __pycache__/
│   ├── data/                   # Data-related scripts and files
│   │   ├── __init__.py
│   │   └── training_data.py    # Training data generation scripts
│   ├── ML_models/              # ML model scripts
│   │   ├── Classifier.py       # Core classifier script
│   │   ├── model.py            # Script for ML model definition and usage
│   │   └── preprocessing.py    # Preprocessing module
│   ├── ml_models_data/         # Folder to store model and vectorizer files
│   │   ├── model.pkl           # Trained model file
│   │   └── vectorizer.pkl      # Trained vectorizer file
│   ├── vectorStore/            # Vector database storage
│   │   ├── index.faiss         # FAISS index for RAG model
│   │   └── index.pkl           # Pickled FAISS index
│   ├── google_search_services.py  # Handles Google Search integration
│   ├── gpt_services.py         # Interacts with GPT APIs
│   ├── scrapping.py            # Scrapping data for RAG training
|   ├── train_model.py          # Model training/updating script
|   ├── urls.py                 # contains urls and routes
│   └── views.py                # Contains function triggered on routes called 
|   
│
└── manage.py                   # Django management script
```

## Environment Variables

Sensitive keys and environment variables are stored in a `.env` file in the `backend/` folder. This file should contain the following variables:

```env
AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
GOOGLE_CSE_ID="YOUR_GOOGLE_CSE_ID"
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
OPENAI_ENDPOINT="YOUR_OPENAI_ENDPOINT"
DEBUG=True
```

> **Note**: Ensure to replace the values above with your respective API keys.

### How to create the `.env` file

1. In the `backend/` folder, create a new file called `.env`.
2. Add the environment variables shown above.
3. Make sure this file is listed in `.gitignore` to avoid committing sensitive data to version control.

## ML Model

The project includes an ML model that predicts three types of responses:
- **LLM**: Leveraging OpenAI's large language model (via Azure).
- **RAG**: Retrieval-Augmented Generation, containing data scraped from the ValeArnis website and stored in a vector database.
- **Internet Search**: Conducts searches on the web using Google Custom Search API.

### Training the Model

The model is initially trained using the script `valearns/train_model.py`. This script can be run to train the model using custom data, and it updates with every user query to improve predictions. The trained files are:
- **model.pkl**: Contains the trained ML model.
- **vectorizer.pkl**: Contains the trained vectorizer.

### Model Limitations
The model is not trained on a large dataset, so predictions may sometimes be inaccurate or biased. Continuous improvements are recommended.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Required libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Shaik-mohd-huzaifa/valearnis-chatbot-assignment.git
cd backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the environment:

Create a `.env` file in the `backend/` directory with the environment variables mentioned above.

4. Run migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

The app should now be running on [http://localhost:8000](http://localhost:8000).

## Model Usage

The ML model is designed to handle different types of predictions:
- **RAG**: Using vector search stored in the `vectorStore/`.
- **LLM**: Using Azure OpenAI GPT models.
- **Internet Search**: Uses Google Custom Search Engine for live queries.

### How to Train the Model

You can train the model using the `train_model.py` script. This will update the `model.pkl` and `vectorizer.pkl` files with new data.

```bash
python valearns/train_model.py
```

## Scraping for RAG

To update the data for the RAG model, use the scraping script in `valearns/scrapping.py`. This will collect data from the ValeArnis website and store it in the vector store.

```bash
python valearns/scrapping.py
```

## License

This project does not currently use any external licenses. However, the predictions made by the ML model are purely based on the data it was trained on, which is not comprehensive. The model may give incorrect or biased responses due to limitations in the dataset.

---

### Replace the environment variables with your own API keys and settings as needed, and modify the folder paths based on your specific use case.
