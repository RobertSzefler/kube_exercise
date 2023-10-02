import os
import socket

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
hostname = socket.gethostname()
mongo_host = os.getenv("MONGO_HOST")
mongo_user = os.getenv("MONGO_USER")
mongo_pass = os.getenv("MONGO_PASSWORD")
mongo_client = MongoClient(mongo_host, username=mongo_user, password=mongo_pass)


@app.route("/", methods=["GET"])
def ctr_get():
    db = mongo_client.testdb
    ctr = db.ctr.find_one()
    if ctr is None:
        # TODO this code should be run upon mongo deployment
        ctr_val = 1
        doc = {"value": ctr_val}
        db.ctr.insert_one(doc)
    else:
        ctr_val = ctr["value"]
    return jsonify(
        {
            "ctr_val": ctr_val,
            "host": hostname,
        }
    )


@app.route("/", methods=["POST"])
def ctr_post():
    db = mongo_client.testdb
    # TODO
    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
