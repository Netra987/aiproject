from itertools import permutations
import re

def validate_equation(equation):
    """Validates the input equation."""
    if not re.match(r'^[A-Z+\-*= ]+$', equation, re.I):
        raise ValueError("Invalid equation: Use only uppercase letters, '+', '-', '*', and '='.")

    if equation.count('=') != 1:
        raise ValueError("Invalid equation: Must contain exactly one '='.")

    if sum(1 for op in equation if op in '+-*') != 1:
        raise ValueError("Invalid equation: Must contain exactly one operator ('+', '-', or '*').")

def solve_cryptarithmetic(equation):
    """Solves the cryptarithmetic equation and provides detailed calculations."""
    equation = equation.replace(" ", "").upper()
    validate_equation(equation)

    left, right = equation.split('=')

    if '+' in left:
        operator = '+'
        left_terms = left.split('+')
    elif '-' in left:
        operator = '-'
        left_terms = left.split('-')
    elif '*' in left:
        operator = '*'
        left_terms = left.split('*')
    else:
        raise ValueError("Invalid equation: Operator not found.")

    letters = set(''.join(left_terms) + right)
    if len(letters) > 10:
        raise ValueError("Too many unique letters. Maximum 10 allowed.")

    leading_letters = {term[0] for term in left_terms + [right]}

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[letter] == 0 for letter in leading_letters):
            continue

        left_values = [int(''.join(str(mapping[char]) for char in term)) for term in left_terms]
        right_value = int(''.join(str(mapping[char]) for char in right))

        # Store detailed calculation steps
        steps = []
        for term, value in zip(left_terms, left_values):
            steps.append(f"{term} → {''.join(str(mapping[char]) for char in term)}")

        steps.append(f"{right} → {right_value}")

        # Final computation
        expression = f"{' + '.join(map(str, left_values))} = {right_value}" if operator == '+' else \
                     f"{left_values[0]} - {left_values[1]} = {right_value}" if operator == '-' else \
                     f"{left_values[0]} * {left_values[1]} = {right_value}"

        if (operator == '+' and sum(left_values) == right_value) or \
           (operator == '-' and left_values[0] - left_values[1] == right_value) or \
           (operator == '*' and left_values[0] * left_values[1] == right_value):
            return {
                "solution": mapping,
                "calculation": {
                    "steps": steps,
                    "expression": expression
                }
            }

    return None
