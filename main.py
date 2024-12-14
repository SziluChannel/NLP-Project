from flask import Flask, request, jsonify
from flask_cors import CORS

from ai import AI

app = Flask(__name__)

# Enable CORS for all domains and all routes
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get the JSON data from the request
    model = data.get('model')
    vectorizer = data.get('vectorizer')
    text = data.get('text')

    resp = AI(model, vectorizer, text)

    # For testing purposes, print the received data
    print(f"Received model: {model}, Vectorizer: {vectorizer} Text: {text}")
    a = format(f"Received model: {model}, Vectorizer: {vectorizer} Text: {text}")
    print(resp)
    # Respond with a success message
    return jsonify({"category": resp})

if __name__ == '__main__':
    app.run(debug=True)
