from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Webhook is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName", "")
    parameters = req.get("queryResult", {}).get("parameters", {})
    
    weight = parameters.get("weight", 0)

    response_text = "Sorry, I couldn't understand the weight."

    if 4.0 <= weight <= 4.4:
        response_text = "Give 120g of B+ daily, 4 packets per month (4 feeds/day)."
    elif 4.5 <= weight <= 6.9:
        response_text = "Give 180g of B+ daily, 5 packets per month (4 feeds/day)."
    elif 7.0 <= weight <= 8.9:
        response_text = "Give 240g of B+ daily, 7 packets per month (4 feeds/day)."
    elif 9.0 <= weight <= 11.4:
        response_text = "Give 340g of B+ daily, 9 packets per month (4 feeds/day)."
    elif weight >= 11.5:
        response_text = "Give 360g of B+ daily, 11 packets per month (4 feeds/day)."

    return jsonify({"fulfillmentText": response_text})
