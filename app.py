from flask import Flask, render_template, request, jsonify
from solver import solve_cryptarithmetic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    equation = data.get('equation', '')
    solution = solve_cryptarithmetic(equation)
    
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)
