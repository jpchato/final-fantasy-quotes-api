from flask import Flask, jsonify
from quotes import quotes

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Final Fantasy Quotes API"

@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes)

@app.route('/quotes/<int:id>', methods=['GET'])
def get_quotes_by_id(id):
    quote = next((quote for quote in quotes if quote['id'] == id), None)
    if quote is not None:
        return jsonify(quote)
    else:
        return jsonify({'error': 'Quote not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
