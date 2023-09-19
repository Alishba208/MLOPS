from flask import Flask, render_template, request, jsonify
#from calculator import Calculator  # Assuming your calculator logic is in a separate file

app = Flask(__name__)

# Initialize your calculator
#calculator = Calculator()

@app.route('/')
def index():
    return "Welcome to the Calculator App"

def add1(num1, num2):
    return num1 + num2


# Define routes for your calculator functions
@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = add1(num1, num2)
    return jsonify({"result": result})

# @app.route('/subtract', methods=['POST'])
# def subtract():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = calculator.subtract(num1, num2)
#     return jsonify({"result": result})

# Add more routes for other calculator functions as needed

if __name__ == '__main__':

    app.run(debug=True, port=8080)
