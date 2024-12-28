from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return jsonify({"message": "Happy New Year 2025!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
