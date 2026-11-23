from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "saas-task-manager"}), 200


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
