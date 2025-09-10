# CSC500 - Module 3 Portfolio Milestone: Online Shopping Cart

## Overview
This project implements a simple online shopping cart that handles two items. Users can input the name, price, and quantity for each item, and the program calculates and displays the total cost. The code includes input validation to handle invalid entries and ensure a robust user experience.

## Features
- Supports entry of two items with name, price, and quantity.
- Validates inputs to prevent negative values and non-numeric entries.
- Formats monetary output (e.g., `$1` or `$2.50`).
- Displays the cost for each item and the total cost.

## How to Run
1. Ensure Python is installed on your system (check with `python --version`).
2. Save the script as `shopping_cart.py` in a directory (e.g., `C:\Users\Bizec\Downloads\meal-and-alarm-program`).
3. Open the directory in Visual Studio Code.
4. Open a terminal in VS Code and navigate to the directory:cd C:\Users\Bizec\Downloads\meal-and-alarm-program
5. Run the script:python shopping_cart.py
6. Follow the prompts to enter item details (name, price, quantity) for two items.

## Example Usage
Item 1
Enter the item name:
Apple
Enter the item price:
2.50
Enter the item quantity:
3
Item 2
Enter the item name:
Banana
Enter the item price:
1
Enter the item quantity:
5
TOTAL COST
Apple 3 @ $2.50 = $7.50
Banana 5 @ $1 = $5
Total: $12.50
## Code Explanation
The program uses a class `ItemToPurchase` to store item details (name, price, quantity) and includes the following logic:
- **Input Handling**: Uses functions (`get_valid_string`, `get_valid_float`, `get_valid_int`) to validate user input, preventing empty strings, negative values, and non-numeric entries. It also handles `EOFError` for interrupted input.
- **Cost Calculation**: Multiplies price by quantity for each item and sums the totals.
- **Output Formatting**: The `fmt_money` function formats monetary values appropriately.
- **Error Handling**: Includes try-catch blocks to manage exceptions like `KeyboardInterrupt` or invalid inputs.

## Pseudocode Reference
Refer to the `pseudocode.txt` file in this directory for a high-level description of the program's logic.

## Requirements
- Python 3.x
- Visual Studio Code (recommended for running and debugging)

## Notes
- Ensure the file is saved before running to avoid "No such file or directory" errors.
- If you encounter an `EOFError`, run the script in the integrated terminal and provide input manually.

## Author
- Stacey Freeman - Date: September 10, 2025

