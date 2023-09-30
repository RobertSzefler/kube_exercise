import socket
import sys

from flask import Flask, jsonify
import requests

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/')
def index():
    # TODO call API
    return 'Hello, World!'


@app.route('/sysinfo')
def sysinfo():
    return jsonify(
        {
            "python_version": sys.version,
            "hostname": hostname,
        }
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
