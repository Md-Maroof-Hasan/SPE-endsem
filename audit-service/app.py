from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    print("AUDIT:", data, flush=True)
    return jsonify({"status": "logged"})

@app.route('/health', methods=['GET'])
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
