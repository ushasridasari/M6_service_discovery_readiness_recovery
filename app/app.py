import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)
ready = True  # toggled at runtime

POD_NAME = os.environ.get("POD_NAME", socket.gethostname())

@app.route("/inventory")
def inventory():
    return jsonify({
        "pod": POD_NAME,
        "items": [
            {"id": 1, "name": "widget", "qty": 42},
            {"id": 2, "name": "gadget", "qty": 17},
        ],
    })

@app.route("/healthz")
def healthz():
    return "alive", 200

@app.route("/ready")
def ready_check():
    if ready:
        return "ready", 200
    return "not ready", 503

@app.route("/toggle-ready", methods=["POST", "GET"])
def toggle_ready():
    global ready
    ready = not ready
    return jsonify({"pod": POD_NAME, "ready": ready})

@app.route("/set-ready/<state>", methods=["POST", "GET"])
def set_ready(state):
    global ready
    ready = (state.lower() == "true")
    return jsonify({"pod": POD_NAME, "ready": ready})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
