from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return 'welcome'


@app.route('/calculate')
def calculate():
    html = render_template('calc.html')
    return html


@app.route('/math')
def math():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operator = request.args.get('operator')
    if operator == 'Add':
        result = num1 + num2
    elif operator == 'Subtract':
        result = num1 - num2
    elif operator == 'Multiply':
        result = num1 * num2
    elif operator == 'Divide':
        result = num1 / num2
    return str(result)
