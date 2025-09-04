# Part 1: Meal Calculator

# Ask user for food charge
food_charge = float(input("Enter the charge for the food: $"))

# Calculate amounts
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Display results
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total amount: ${total:.2f}")
