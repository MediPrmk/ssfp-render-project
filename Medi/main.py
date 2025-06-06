from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    try:
        weight = extract_weight(req)
        response_text = get_balamrutham_dosage(weight)
    except Exception as e:
        response_text = "Sorry, I couldn't process the weight. Please try again."

    return jsonify({"fulfillmentText": response_text})

def extract_weight(req):
    params = req.get("queryResult", {}).get("parameters", {})
    numbers = params.get("number", [])
    if isinstance(numbers, list) and numbers:
        return float(numbers[0])
    elif isinstance(numbers, float) or isinstance(numbers, int):
        return float(numbers)
    raise ValueError("Weight not found.")

def get_balamrutham_dosage(weight):
    if weight < 4.5:
        return "For 4.0 to 4.4 kg: 120g/day → 4 packets/month"
    elif 4.5 <= weight <= 6.9:
        return "For 4.5 to 6.9 kg: 180g/day → 5 packets/month"
    elif 7.0 <= weight <= 8.9:
        return "For 7.0 to 8.9 kg: 240g/day → 7 packets/month"
    elif 9.0 <= weight <= 11.4:
        return "For 9.0 to 11.4 kg: 340g/day → 9 packets/month"
    elif weight >= 11.5:
        return "For 11.5+ kg: 360g/day → 11 packets/month"
    else:
        return "Please enter a valid weight."

if __name__ == "__main__":
    app.run()
