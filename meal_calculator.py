
# Part 1: Meal Calculator
try:
    food_charge = float(input("Enter the charge for the food (e.g., 50.00): "))
    if food_charge < 0:
        raise ValueError("Charge must be non-negative")
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Calculate amounts
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Display results
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total amount: ${total:.2f}")