from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud Optimizer ENV Running"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({
        "message": "Environment reset successful",
        "state": {"cpu": 50, "memory": 50}
    })

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action", "do_nothing")

    reward = 0
    done = False

    if action == "scale_up":
        reward = -1
    elif action == "scale_down":
        reward = 1
    elif action == "do_nothing":
        reward = 0.5

    return jsonify({
        "reward": reward,
        "done": done,
        "state": {"cpu": 60, "memory": 40}
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)