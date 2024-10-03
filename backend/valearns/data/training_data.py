train_data = [
    ("What is quantum mechanics?", "LLM"),  # Use LLM for general knowledge explanation
    ("Latest AI news", "Internet Search"),  # Web search required for recent news
    ("How does the blockchain work?", "LLM"),  # Use LLM for conceptual explanation
    ("Weather in New York today", "Internet Search"),  # Web search for real-time data
    ("Can you explain the big bang theory?", "LLM"),  # LLM for scientific concepts
    (
        "Who won the football match yesterday?",
        "Internet Search",
    ),  # Web search for recent events
    (
        "What are the current Student number enrolled in 7th grade courses",
        "RAG",
    ),  # RAG for detailed information retrieval
    (
        "Does Basic Math include in 1st Grade syllabus",
        "RAG",
    ),  # RAG for sourcing multiple viewpoints
    (
        "Tell me about the best programming languages for AI development",
        "LLM",
    ),  # LLM for opinion-based knowledge
    (
        "What is the latest research on climate change?",
        "Internet Search",
    ),  # Web search for up-to-date research
    (
        "Who is the Education Minister of India",
        "LLM",
    ),  # LLM for general knowledge on health
    ("What is the Syllabus for Grade 7?", "RAG"),  # RAG for analyzing multiple sources
    (
        "Which companies are leading the AI revolution?",
        "Internet Search",
    ),  # Web search for current data on companies
    (
        "What is per month cost of 7th grade course/subscription",
        "RAG",
    ),  # RAG for historical data and aggregation
    ("Who is the Father of Indian Nation", "Internet Search"),
    ("What is Pricing of subscription at valearnis", "RAG"),
    ("What is Valeanis?", "RAG"),
    ("Who Won the t20 World Cup 2024", "Internet Search"),
    ("Who is the Fathe of Indian Nation", "LLM"),
    ("Who is the Current Prime Minister of India", "Internet Search"),
    (
        "What will be the height of a banayan tree after 10 years if i plant it now",
        "LLM",
    ),
    ("Richest man on the World", "Internet Search"),
    ("Sucrose vs glucose difference", "LLM"),
]

# train_data = [
#     ("What is quantum mechanics?", 0),  # 0 -> General chat, use GPT-4
#     ("Latest AI news", 1),  # 1 -> Web search required
#     ("How does the blockchain work?", 0),
#     ("Weather in New York today", 1),
#     ("Can you explain the big bang theory?", 0),
#     ("Who won the football match yesterday?", 1),
#     ("How much time does it take a baniyan tree to grow 20ft tall", 0),
# ]
