from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "4b1a0e44-0205-4ad8-9158-3c10c3e87ae9"


@app.route('/api/news', methods=['GET'])
def hello_world():
    api_key = request.args.get('api_key')

    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    message = {"message": "Demo"}
    return jsonify(message)


if __name__ == '__main__':
    app.run()
