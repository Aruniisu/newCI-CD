# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/status")
def status():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(debug=True)
