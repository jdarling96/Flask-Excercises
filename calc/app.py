# Put your app in here.
from flask import Flask, request
from operations import add


app = Flask(__name__)

@app.route("/add")
def add_numbers():
    
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(add(a,b))



