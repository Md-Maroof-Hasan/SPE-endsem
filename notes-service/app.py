from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

notes = []

AUTH_SERVICE_URL = "http://auth-service:5001"
AUDIT_SERVICE_URL = "http://audit-service:5003"

def validate_token(token):
    try:
        res = requests.post(
            f"{AUTH_SERVICE_URL}/validate",
            json={"token": token}
        )

        if res.status_code == 200:
            return res.json().get("user")

    except:
        pass

    return None

def send_audit_log(user, action, content):
    try:
        requests.post(
            f"{AUDIT_SERVICE_URL}/log",
            json={
                "user": user,
                "action": action,
                "content": content
            }
        )
    except:
        print("Audit service unavailable")

@app.route('/notes', methods=['POST'])
def create_note():

    token = request.headers.get("Authorization")

    user = validate_token(token)

    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    note = {
        "id": len(notes) + 1,
        "user": user,
        "content": data.get("content")
    }

    notes.append(note)

    # Send log to audit-service
    send_audit_log(user, "CREATE_NOTE", note["content"])

    return jsonify(note)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/health', methods=['GET'])
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
