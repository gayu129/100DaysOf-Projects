from flask import Flask, request, render_template
import pickle
import random

app = Flask(__name__)

# Load trained components
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
responses = pickle.load(open('responses.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.form['msg']
    user_input_transformed = vectorizer.transform([user_input.lower()])
    prediction = model.predict(user_input_transformed)[0]
    response_list = responses[prediction]
    return random.choice(response_list)

if __name__ == '__main__':
    app.run(debug=True)
