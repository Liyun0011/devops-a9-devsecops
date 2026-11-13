# DEMO ONLY - deliberately vulnerable Flask app for CodeQL (SAST) to find.
# Never run or deploy this.
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # Command injection: user input goes straight into a shell command
    out = subprocess.check_output("ping -c 1 " + host, shell=True)
    return out


@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    # Reflected XSS: user input returned as HTML without escaping
    return "<h1>Hello " + name + "</h1>"
