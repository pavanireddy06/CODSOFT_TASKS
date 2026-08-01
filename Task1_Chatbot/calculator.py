"""
calculator.py
--------------
Safe calculator module for the Rule-Based Chatbot.
Supports:
+  Addition
-  Subtraction
*  Multiplication
/  Division

Does NOT use eval(), making it safer and interview-friendly.
"""

import operator
import re

# Dictionary of supported operations
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def calculate(expression):
    """
    Calculates a simple mathematical expression.

    Examples:
        10+20
        25*4
        100/5
        80-15
    """

    # Remove spaces
    expression = expression.replace(" ", "")

    # Regular expression for number operator number
    pattern = r"(-?\d+\.?\d*)([\+\-\*/])(-?\d+\.?\d*)"

    match = re.fullmatch(pattern, expression)

    if not match:
        return "❌ Invalid expression.\nExample: calculate 25*10"

    num1, operator_symbol, num2 = match.groups()

    num1 = float(num1)
    num2 = float(num2)

    # Prevent divide by zero
    if operator_symbol == "/" and num2 == 0:
        return "❌ Cannot divide by zero."

    result = OPERATIONS[operator_symbol](num1, num2)

    # Remove .0 if integer
    if result.is_integer():
        return int(result)

    return round(result, 2)


# ------------------------------
# Testing
# ------------------------------

if __name__ == "__main__":

    while True:

        exp = input("Enter Expression (or exit): ")

        if exp.lower() == "exit":
            break

        print("Answer :", calculate(exp))