from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaOfcircle():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = 3.14 * radius * radius
    return render_template('areaofcircle.html', area=area)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('areaoftriangle.html', area=area)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    works_list = [
        {'name': 'toUpperCase', 'url': '/touppercase'},
        {'name': 'Area of Circle', 'url': '/areaofcircle'},
        {'name': 'Area of Triangle', 'url': '/areaoftriangle'},
        {'name': 'Infix to Postfix', 'url': '/infix_postfix'},
    ]
    return render_template('works.html', works=works_list)

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []
    for token in expression.replace(' ', ''):
        if token.isalnum():   
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 
        else: 
            while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

@app.route('/infix_postfix', methods=['GET', 'POST'])
def infix_postfix():
    result = None
    if request.method == 'POST':
        infix_expr = request.form.get('infix_expression', '')
        if infix_expr:
            result = infix_to_postfix(infix_expr)
    return render_template('infix_postfix.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
