import socket

from flask import Flask, jsonify

app = Flask(__name__)
hostname = socket.gethostname()


@app.route("/", methods=["GET"])
def ctr_get():
    ctr_val = 13  # TODO
    return jsonify({"ctr_val": ctr_val, "host": hostname})


@app.route("/", methods=["POST"])
def ctr_post():
    # TODO
    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
