# Part 2: Book Club Points Program

# Ask for number of books
books = int(input("Enter the number of books purchased this month: "))

# Determine points
if books == 0:
    points = 0
elif books == 2:
    points = 5
elif books == 4:
    points = 15
elif books == 6:
    points = 30
elif books >= 8:
    points = 60
else:
    points = 0  # For odd numbers not in the chart

# Display points
print("\n--- Book Club Points ---")
print(f"Books purchased: {books}")
print(f"Points awarded: {points}")
