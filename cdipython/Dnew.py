#!/usr/bin/env python3
# Initialize variables
month_steps = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
month_days_over_10000 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Read data from Steps.txt file and skip lines starting with #
with open("Steps.txt", "r") as file:
    steps_data = file.read().splitlines()

# Calculate the average steps and count days with steps > 10,000 per month
for day in steps_data:
    if not day.startswith("#"):  # Skip lines starting with #
        day_number, steps = map(int, day.split(","))
        month = (day_number - 1) // 30 + 1  # Calculate the month based on the day number
        if 1 <= month <= 12:  # Check if the month is within the valid range
            month_steps[month].append(steps)
            if steps >= 10000:
                month_days_over_10000[month] += 1

# Display the average steps and count of days with steps > 10,000 per month
for month in month_steps:
    steps_list = month_steps[month]
    days_over_10000 = month_days_over_10000[month]
    if steps_list:
        average_steps = sum(steps_list) / len(steps_list)
        print(f"Month {month}: Average Steps: {average_steps:.2f}, Days > 10,000: {days_over_10000}")
    else:
        print(f"Month {month}: No data available, Days > 10,000: {days_over_10000}")

