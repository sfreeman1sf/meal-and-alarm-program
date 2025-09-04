# Part 2: Alarm Clock

# Ask user for inputs
current_time = int(input("Enter the current time (0-23): "))
wait_time = int(input("Enter the number of hours to wait: "))

# Calculate alarm time
alarm_time = (current_time + wait_time) % 24

# Display result
print(f"The alarm will go off at {alarm_time}:00 hours (24-hour clock).")
# End of Part 2
