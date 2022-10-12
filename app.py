from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    return "welcome"

@app.get('/welcome/home')
def welcome_home():
    return "welcome home"