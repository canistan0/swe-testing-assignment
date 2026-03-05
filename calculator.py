# calculator.py - The brain of Quick-Calc

def add(a, b):
    """Adds two numbers together"""
    return a + b

def subtract(a, b):
    """Subtracts b from a"""
    return a - b

def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

def divide(a, b):
    """Divides a by b. Returns error message if dividing by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def clear():
    """Resets everything to zero"""
    return 0



