#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(f"{parameter}")
    return(f"{parameter}")

@app.route('/count/<int:parameter>')
def count_parameter(parameter):
    count = f''
    for n in range(parameter):
        count += f'{n}\n'
    return count
    
@app.route('/math/<num1>/<oper>/<num2>')
def math(num1, oper, num2):
    if f"{oper}" == "+":
        return f"{int(num1) + int(num2)}"
    elif f"{oper}" == "-":
        return f"{int(num1) - int(num2)}"
    elif f"{oper}" == "*":
        return f"{int(num1) * int(num2)}"
    elif f"{oper}" == "div":
        print("div")
        return f"{int(num1) / int(num2)}"
    elif f"{oper}" == "%":
        return f"{int(num1) % int(num2)}"
