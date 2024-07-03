from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module

app = Flask(__name__)
CORS(app)  # Apply CORS to your Flask appk

# Sample data - list of gifts
gifts = [
        {"id": 1, "name": "Apple Airtag(s)", "link": "https://a.co/d/02GbecVz", "comment": ""},
    {"id": 2, "name": "Amazon Gift Card", "link": "https://a.co/d/02GbecVz", "comment": "You literally can't go wrong with this one."},

]

# Route to serve the list of gifts
@app.route('/api/gifts', methods=['GET'])
def get_gifts():
    return jsonify(gifts)

if __name__ == '__main__':
    app.run(debug=True)
