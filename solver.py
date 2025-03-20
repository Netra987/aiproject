from itertools import permutations
import re


def validate_equation(equation):
    if not re.match(r'^[A-Z+\-*= ]+$', equation, re.I):
        raise ValueError("Invalid equation: Use only uppercase letters, '+', '-', '*', and '='.")

    if equation.count('=') != 1:
        raise ValueError("Invalid equation: Must contain exactly one '='.")

    if sum(1 for op in equation if op in '+-*') != 1:
        raise ValueError("Invalid equation: Must contain exactly one operator ('+', '-', or '*').")


def solve_cryptarithmetic(equation):
    equation = equation.replace(" ", "").upper()  # Remove spaces and normalize case
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
            continue  # Skip invalid mappings with leading zeros

        left_values = [int(''.join(str(mapping[char]) for char in term)) for term in left_terms]
        right_value = int(''.join(str(mapping[char]) for char in right))

        if operator == '+' and sum(left_values) == right_value:
            return mapping
        elif operator == '-' and left_values[0] - left_values[1] == right_value:
            return mapping
        elif operator == '*' and left_values[0] * left_values[1] == right_value:
            return mapping

    return None


def display_solution(equation, solution):
    if not solution:
        print("No solution exists.")
        return

    print("\nSolution found:")
    for letter, digit in sorted(solution.items()):
        print(f"{letter}: {digit}")

    replaced_equation = equation
    for letter, digit in solution.items():
        replaced_equation = replaced_equation.replace(letter, str(digit))
    
    print(f"\n{equation} -> {replaced_equation} (Valid)")


if __name__ == "__main__":
    print("Cryptarithmetic Problem Solver")
    print("Example: SEND + MORE = MONEY")
    
    try:
        equation = input("Enter the cryptarithmetic equation: ").strip()
        solution = solve_cryptarithmetic(equation)
        display_solution(equation, solution)
    except ValueError as e:
        print(f"Error: {e}")
