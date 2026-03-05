import pytest
from calculator import add, subtract, multiply, divide, clear

def test_add_positive_numbers():
    assert add(5, 3) == 8
def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_subtract_basic():
    assert subtract(10, 4) == 6
def test_subtract_result_negative():
    assert subtract(3, 7) == -4



def test_multiply_basic():
    assert multiply(6, 7) == 42
def test_multiply_by_zero():
    assert multiply(5, 0) == 0



def test_divide_basic():
    assert divide(10, 2) == 5.0
def test_divide_by_zero():
    assert divide(10, 0) == "Error: Division by zero"



def test_add_decimal_numbers():
    assert add(1.5, 2.5) == 4.0

def test_divide_large_numbers():
    assert divide(1000000, 500000) == 2.0


def test_clear_returns_zero():
    assert clear() == 0
