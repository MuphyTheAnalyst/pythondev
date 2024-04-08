#!/usr/bin/env python3

# Read data from Steps.txt file
with open("Steps.txt", "r") as file:
    steps_data = file.read().splitlines()

# Initialize variables
day_steps = {}
days_over_10000 = {}

# Calculate the average steps and count days with steps > 10000 for each day
for line in steps_data:
    if line.strip():  # Check if the line is not empty
        day, steps = map(int, line.split(","))
        day_steps[day] = steps
        if steps > 10000:
            days_over_10000[day] = 1

# Display the average steps and count of days with steps > 10000
for day, steps in day_steps.items():
    day_over_10000 = days_over_10000.get(day, 0)
    print(f"Day {day}: Steps: {steps}, Steps > 10,000: {day_over_10000}")

