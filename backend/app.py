# from flask import Flask, request, jsonify
# import base64
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# app = Flask(__name__)
# @app.route('/bfhl', methods=['GET'])
# def get_operation_code():
#     return jsonify({"operation_code": 1}), 200

# @app.route('/bfhl', methods=['POST'])
# def process_data():
#     try:
#         data = request.get_json()
#         if not data or 'data' not in data:
#             return jsonify({"is_success": False, "error": "'data' is required"}), 400

#         input_data = data.get('data', [])
#         file_b64 = data.get('file_b64', '')

#         # Input validation
#         if not isinstance(input_data, list):
#             return jsonify({"is_success": False, "error": "'data' should be a list"}), 400

#         # Separate numbers and alphabets
#         numbers = [item for item in input_data if item.isdigit()]
#         alphabets = [item for item in input_data if item.isalpha()]

#         # Find highest lowercase alphabet
#         lowercase_alphabets = [char for char in alphabets if char.islower()]
#         if lowercase_alphabets:
#             highest_lowercase = [max(lowercase_alphabets)]
#         else:
#             highest_lowercase = []

#         # Handle file
#         if file_b64:
#             try:
#                 file_data = base64.b64decode(file_b64)
#                 file_valid = True

#                 # Since we can't determine the MIME type without additional libraries,
#                 # we'll set a placeholder value.
#                 file_mime_type = "application/octet-stream"

#                 # Calculate file size in KB
#                 file_size_kb = len(file_data) / 1024
#                 file_size_kb = f"{file_size_kb:.2f}"
#             except Exception:
#                 file_valid = False
#                 file_mime_type = None
#                 file_size_kb = None
#         else:
#             file_valid = False
#             file_mime_type = None
#             file_size_kb = None

#         response = {
#             "is_success": True,
#             "user_id": "john_doe_17091999",
#             "email": "john@xyz.com",
#             "roll_number": "ABCD123",
#             "numbers": numbers,
#             "alphabets": alphabets,
#             "highest_lowercase_alphabet": highest_lowercase,
#             "file_valid": file_valid,
#             "file_mime_type": file_mime_type,
#             "file_size_kb": file_size_kb
#         }
#         return jsonify(response), 200
#     except Exception as e:
#         return jsonify({"is_success": False, "error": str(e)}), 400
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json
        # Your logic for handling the request goes here
        return jsonify({"message": "Data received", "data": data})

    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)





@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({"is_success": False, "error": "'data' is required"}), 400

        input_data = data.get('data', [])
        file_b64 = data.get('file_b64', '')

        # Input validation
        if not isinstance(input_data, list):
            return jsonify({"is_success": False, "error": "'data' should be a list"}), 400

        # Separate numbers and alphabets
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]

        # Find highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        if lowercase_alphabets:
            highest_lowercase = [max(lowercase_alphabets)]
        else:
            highest_lowercase = []

        # Handle file
        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_valid = True

                # Since we can't determine the MIME type without additional libraries,
                # we'll set a placeholder value.
                file_mime_type = "application/octet-stream"

                # Calculate file size in KB
                file_size_kb = len(file_data) / 1024
                file_size_kb = f"{file_size_kb:.2f}"
            except Exception:
                file_valid = False
                file_mime_type = None
                file_size_kb = None
        else:
            file_valid = False
            file_mime_type = None
            file_size_kb = None

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400
