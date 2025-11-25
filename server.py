# License server for validating product keys
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Example license keys and expiration dates (Unix timestamp)
valid_keys = {
    "ABC123-XYZ789": {"expires_at": 1767225600},  # Jan 31, 2026
    "DEF456-GHI012": {"expires_at": 1767225600},
}

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    key = data.get("key")
    info = valid_keys.get(key)
    if info and info["expires_at"] > time.time():
        return jsonify({"valid": True, "expires_at": info["expires_at"]})
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
