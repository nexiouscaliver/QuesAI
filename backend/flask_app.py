# import flask
# #abhi handle the request

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'

if __name__=='main':
    app.run()