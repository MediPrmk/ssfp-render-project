from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "SSFP Webhook is running."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    return jsonify({'received': data})
