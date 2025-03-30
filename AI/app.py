from flask import Flask, render_template, request, jsonify
from solver import solve_cryptarithmetic
import random

app = Flask(__name__)

# List of 50 equations (40 solvable, 10 unsolvable)
equations = [
    "SEND + MORE = MONEY", "BASE + BALL = GAMES", "RAIN + BOW = COLORS",
    "FIRE + WOOD = SMOKE", "TWO + TWO = FOUR", "FIVE * FIVE = TWENTYFIVE",
    "EAT + MEAL = DINNER", "TEN + TEN = TWENTY", "SUN + SKY = BRIGHT",
    "OIL + HEAT = ENERGY", "TEAM + WORK = SUCCESS", "ONE + ONE = TWO",
    "CODE + CODE = DEBUG", "JUMP + OVER = HURDLE", "FLOW + RIVER = WATER",
    "SIX + FOUR = TEN", "PINK + BLUE = COLORS", "NINE + ONE = TEN",
    "LEAF + TREE = FOREST", "BOOK + PAGE = STORY", "GOLD + COIN = WEALTH",
    "STAR + NIGHT = BRIGHT", "FAST + SPEED = QUICK", "MATH + CLASS = SCHOOL",
    "APPLE + TREE = ORCHARD", "TALL + SHORT = HEIGHT", "RED + GREEN = COLOR",
    "FISH + WATER = OCEAN", "BIRD + SKY = FLY", "LIGHT + DARK = SHADE",
    "COLD + SNOW = WINTER", "HEAVY + LIGHT = WEIGHT", "HARD + WORK = SUCCESS",
    "MIND + THINK = IDEA", "RICH + POOR = MONEY", "DAY + NIGHT = TIME",
    "LION + CUB = FAMILY", "TRAIN + TRACK = RAIL", "SLOW + FAST = SPEED",
    "HAPPY + SMILE = JOY",  # 40 solvable

    "ABC + DEF = GHIJK",  # More than 10 unique letters
    "HELLO + WORLD = PYTHON",  # More than 10 unique letters
    "ABCDE + FGHIJ = KLMNO",  # More than 10 unique letters
    "AAA + BBB = CCC",  # No unique solution
    "ONE * TWO = THREE",  # Incorrect multiplication
    "LARGE - SMALL = NEGATIVE",  # Negative result
    "SEVEN + EIGHT = FIFTEENZ",  # Extra character at end
    "TWELVE + TWELVE = TWENTYFOUR",  # More than 10 unique letters
    "AAA * AAA = BBBB",  # Too large result
    "ABCD + EFGH = IJKLMNOP"  # Too many letters
]

current_index = -1  # Track the current equation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_equation', methods=['GET'])
def get_equation():
    global current_index
    current_index += 1
    if current_index >= len(equations):
        return jsonify({'error': 'No more equations available'})
    return jsonify({'equation': equations[current_index]})

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    equation = data.get('equation', '')
    solution = solve_cryptarithmetic(equation)

    if solution:
        return jsonify(solution)
    else:
        return jsonify({'error': 'No solution found'})

if __name__ == '__main__':
    app.run(debug=True)
