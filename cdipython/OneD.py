#!/usr/bin/env python3

# Read data from Steps.txt file
with open("Steps.txt", "r") as file:
    steps_data = file.read().splitlines()

# Initialize variables
month_steps = {}
days_10000_or_more = 0

# Calculate the average steps per month
for day in steps_data:
    if day.strip():  # Check if the line is not empty
        month, steps = map(int, day.split(","))
        
        # Check if the month is already in the dictionary, and if not, add it.
        if month not in month_steps:
            month_steps[month] = {"total_steps": steps, "days_count": 1}
        else:
            month_steps[month]["total_steps"] += steps
            month_steps[month]["days_count"] += 1

        if steps >= 10000:
            days_10000_or_more += 1

# Display the average steps per month
for month in sorted(month_steps.keys()):
    data = month_steps[month]
    average_steps = data["total_steps"] / data["days_count"]
    print(f"Month {month}: Average Steps: {average_steps:.2f}")

# Display the number of days with 10,000 or more steps
print(f"Number of days with 10,000 or more steps: {days_10000_or_more}")

