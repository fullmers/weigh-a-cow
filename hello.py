from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_team():
    return "<p>Hello, Team!</p>" 