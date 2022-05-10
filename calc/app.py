# Put your app in here.
from flask import Flask, request
from operations import *


app = Flask(__name__)

@app.route("/add")
def add_numbers():
    
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(add(a,b))

@app.route('/sub')
def sub_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a,b))

@app.route('/mult')
def mult_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a,b))

@app.route('/div')
def divide_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a,b))






@app.route('/math/<id>')
def find_operation(id):
    
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    number_operations={
    'add': add(a,b),
    'sub': sub(a,b),
    'mult': mult(a,b),
    'div': div(a,b)
}
  
    math = number_operations[id]
    
    return str(math) 
