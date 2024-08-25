from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for response (You should replace these with actual values or inputs)
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        try:
            # Parse input JSON
            input_data = request.json.get('data', [])
            
            # Initialize arrays for numbers and alphabets
            numbers = []
            alphabets = []
            highest_lowercase_alphabet = []

            # Separate numbers and alphabets
            for item in input_data:
                if item.isdigit():
                    numbers.append(item)
                elif item.isalpha():
                    alphabets.append(item)
                    if item.islower():
                        highest_lowercase_alphabet.append(item)

            # Find the highest lowercase alphabet if exists
            highest_lowercase_alphabet = [max(highest_lowercase_alphabet)] if highest_lowercase_alphabet else []

            response = {
                "is_success": True,
                "user_id": USER_ID,
                "email": EMAIL,
                "roll_number": ROLL_NUMBER,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet
            }
            return jsonify(response), 200

        except Exception as e:
            # Return error response in case of exceptions
            return jsonify({"is_success": False, "error": str(e)}), 400

    elif request.method == 'GET':
        # Hardcoded response for GET request
        return jsonify({"operation_code": 1}), 200


if __name__ == '__main__':
    app.run(debug=True)
