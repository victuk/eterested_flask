# topic_extractor.py
from transformers import pipeline
from collections import Counter
import re

print("Running")

# Initialize the NLP pipeline for named entity recognition
nlp = pipeline("ner", aggregation_strategy="simple")

def extract_topics(text):
    # Preprocess the text
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.strip()

    # Use the NLP model to get entities
    entities = nlp(text)

    # Extract unique words from entities
    topics = [entity['word'] for entity in entities]
    unique_topics = list(Counter(topics).keys())  # Get unique topics

    return unique_topics

# if __name__ == "__main__":
sample_text = (
    "Natural language processing is a fascinating field of artificial intelligence."
    " It enables computers to understand and generate human language."
)
topics = extract_topics(sample_text)
print("Extracted Topics:", topics)

# pip install transformers torch