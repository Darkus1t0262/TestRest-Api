# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola Mundo desde REST API!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)