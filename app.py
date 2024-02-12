from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC By Ceylan B. (<a href='https://hackerone.com/ceylan'>https://hackerone.com/ceylan</a>)"
