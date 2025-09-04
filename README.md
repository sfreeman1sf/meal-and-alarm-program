# CSC500 Module 3: Meal and Alarm Programs

This repository contains two Python programs for the CSC500 Module 3 Critical Thinking assignment. The programs implement a meal cost calculator and a 24-hour alarm clock calculator, meeting the requirements to calculate costs with tip/tax and time with modulo arithmetic.

## Project Overview
- **Part 1: Meal Calculator**: Prompts for a food charge, calculates an 18% tip and 7% sales tax, and displays the breakdown and total, formatted to two decimal places.
- **Part 2: Alarm Clock**: Prompts for the current time (0–23) and hours to wait, calculates the alarm time in 24-hour format, and includes days for large wait times.
- **Submission**: Includes pseudocode, source code, screenshots, and this Git repository, submitted in a Word document.



## Part 1: Meal Calculator
### Description
- Prompts user for the food charge (e.g., 50.00).
- Calculates:
  - Tip: 18% of food charge
  - Sales tax: 7% of food charge
  - Total: Food charge + tip + tax
- Validates non-negative input (exits on negative).
- Displays amounts formatted to two decimal places.

### Run
```bash
python meal_calculator.py

### Example output
Enter the charge for the food (e.g., 50.00): 50
Food charge: $50.00
Tip (18%): $9.00
Tax (7%): $3.50
Total amount: $62.50
---

## Part 2: Alarm Clock
Description

Prompts for current time (0–23) and hours to wait.
Calculates alarm time using modulo 24 for hours.
Displays days if wait time exceeds 24 hours.
Validates time (0–23) and non-negative wait time (exits on invalid).
Outputs time in HH:00 format (24-hour).

### Run
```bash
python alarm_clock.py

### Example output
Enter the current time (0-23): 13
Enter the number of hours to wait: 50
The alarm will go off at 15:00 in 2 day(s) (24-hour format).

## Files

meal_calculator.py: Source code for Part 1.
alarm_clock.py: Source code for Part 2.
README.md: This file.