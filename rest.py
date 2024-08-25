# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])

    if not isinstance(data, list):
        return jsonify({"is_success": False, "error": "Invalid data format"}), 400

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = sorted(lowercase_alphabets)[-1:] if lowercase_alphabets else []

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
