from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/addition")
def addition():
    return jsonify({"result": 5})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
