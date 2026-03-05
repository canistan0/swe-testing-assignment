# Testing Strategy for Quick-Calc

## Overview

This document describes the testing approach used for the Quick-Calc calculator application.

## What Was Tested (and What Wasn't)

**Tested:**

- All four arithmetic operations (add, subtract, multiply, divide)
- Edge cases: division by zero, negative numbers, decimals, large numbers
- The clear/reset functionality
- Integration between user input flow and calculation logic

**Not Tested:**

- Performance under extreme load
- UI rendering (no graphical interface exists to test)
- Security vulnerabilities

## Lecture Concepts Applied

### 1. The Testing Pyramid

The Testing Pyramid suggests having many unit tests at the base, fewer integration tests in the middle, and even fewer end-to-end tests at the top. This project reflects that: **11 unit tests** form the base , and **2 integration tests** sit above. No end-to-end UI tests exist since the app is command-line based.

### 2. Black-box vs White-box Testing

**Unit tests** used a **white-box** approach — I wrote them knowing the internal code. **Integration tests** used a **black-box** approach — they simulate a user's perspective without caring about the internal implementation details.

### 3. Functional vs Non-Functional Testing

All tests in this project are **functional** — they verify the calculator _does what it's supposed to do_. **Non-functional** qualities like performance, reliability under load, or memory usage were intentionally not tested, as they are not meaningful for a lightweight calculator application.

### 4. Regression Testing

The test suite acts as a **regression safety net**. If a future developer modifies the `divide` function , running `pytest` immediately would catch any accidental breakage in existing behaviour. The meaningful commit history also allows rollback to any previous working state.
