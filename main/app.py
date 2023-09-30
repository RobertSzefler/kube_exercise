import os
import socket
import sys

from flask import Flask, jsonify
import requests

app = Flask(__name__)
hostname = socket.gethostname()
api_url = os.getenv("API_URL")


@app.route("/", methods=["GET"])
def index_get():
    # TODO call API
    resp = requests.get(api_url)
    if resp.ok:
        data = resp.json()
        ctr_val = data["ctr_val"]
        api_host = data["host"]
        return f"The counter value is: {ctr_val}, got response from {api_host}"
    else:
        return f"API call failed"


@app.route("/", methods=["POST"])
def index_post():
    # TODO call API
    return "OK"


@app.route("/sysinfo")
def sysinfo():
    return jsonify(
        {
            "python_version": sys.version,
            "hostname": hostname,
            "api_url": api_url,
        }
    )


@app.route("/error", methods=["GET"])
def error():
    raise Exception


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
