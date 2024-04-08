#!/usr/bin/env python3

# Read data from Steps.txt file
with open("Steps.txt", "r") as file:
    steps_data = file.read().splitlines()

# Initialize variables
month_steps = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}

# Calculate the average steps per month
for day in steps_data:
    if day.strip():  # Check if the line is not empty
        month, steps = map(int, day.split(","))
        if 1 <= month <= 12:  # Check if the month is within the valid range
            month_steps[month].append(steps)

# Display the average steps per month
for month, steps_list in month_steps.items():
    if steps_list:
        average_steps = sum(steps_list) / len(steps_list)
        print(f"Month {month}: Average Steps: {average_steps:.2f}")
    else:
        print(f"Month {month}: No data available")

