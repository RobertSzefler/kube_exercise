from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/items')
def items():
    items = []  # TODO
    return jsonify(items)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)