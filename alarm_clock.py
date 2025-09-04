# Part 2: Alarm Clock
try:
    current_time = int(input("Enter the current time (0-23): "))
    if not 0 <= current_time <= 23:
        raise ValueError("Time must be between 0 and 23")
    wait_time = int(input("Enter the number of hours to wait: "))
    if wait_time < 0:
        raise ValueError("Hours must be non-negative")
except ValueError:
    print("Invalid input! Please enter valid integers.")
    exit()

# Calculate alarm time
total_hours = (current_time + wait_time) % 24
days = (current_time + wait_time) // 24

# Display result
if days > 0:
    print(f"The alarm will go off at {total_hours:02d}:00 in {days} day(s) (24-hour format).")
else:
    print(f"The alarm will go off at {total_hours:02d}:00 (24-hour format).")
