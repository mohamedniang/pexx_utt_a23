from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World !"

@app.route("/abt")
def about():
    return "This is the about page 😀"