# swe-testing-assignment

# Quick-Calc 

A simple command-line calculator application that supports addition, subtraction, multiplication, and division. Built as part of a software testing assignment to demonstrate unit testing, integration testing, and version control best practices.

## Setup Instructions

1. install Python 3 
2. Clone this repository
3. Install pytest
4. Run the application

## Run Tests

Run all tests with pytest

## Testing Framework Research

### Pytest vs Unittest

**Unittest** is Python's built-in testing framework, included with every Python installation. Its main advantage is that no installation is required — it works out of the box. It follows a class-based structure, which makes it familiar to developers coming from other languages. However, this structure adds boilerplate: even simple tests require creating a class and calling `self.assert...` methods, which can make tests feel verbose and harder to read for beginners.

**Pytest** is a third-party framework that has become the industry standard for Python testing. Its biggest advantage is simplicity: tests are plain functions, and assertions use Python's native `assert` keyword. This makes tests far more readable and writable. Pytest also offers powerful features like fixtures, parametrize, and detailed failure messages that pinpoint exactly what went wrong.

**Choice:** I chose **Pytest** for this project because of its readability and simplicity. For a calculator project focused on clean, understandable tests, Pytest's plain-function style makes the test intent immediately clear to any reader. The `pip3 install pytest` setup cost is minimal compared to the readability gains.
