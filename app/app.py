from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "Day 8 Helm Kubernetes CI/CD",
        "version": "1.0.0",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/ready")
def ready():
    return jsonify({"status": "ready"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
