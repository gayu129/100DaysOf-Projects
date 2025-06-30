import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt')

# Load dataset
with open('data.json') as file:
    data = json.load(file)

corpus = []
tags = []
tag_responses = {}

for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern.lower())
        tags.append(intent['tag'])
    tag_responses[intent['tag']] = intent['responses']

# No custom tokenizer — use default
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
y = np.array(tags)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and files
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
pickle.dump(tag_responses, open('responses.pkl', 'wb'))

print("✅ Model trained and saved successfully!")
