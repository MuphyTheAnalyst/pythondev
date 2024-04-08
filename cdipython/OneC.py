#!/usr/bin/env python3
#A painting company has determined that for every 112 square feet of wall space, one
#gallon of paint is required. The company charges $25.00 per hour for labour. Write a
#program that asks the user to enter the number of square feet of wall space to be
#painted and the price of the paint per gallon. The program should then display the
#following data.
# The number of gallons of paint required
# The cost of the paint
# The hours of labour required to complete the job
# The cost of the labour to complete the job
# The total cost of the paint job.

# Input from the user
square_feet = float(input("Enter the number of square feet to be painted: "))
price_per_gallon = float(input("Enter the price of paint per gallon: "))

# Constants
paint_needed_per_square_foot = 1 / 112
labor_rate_per_hour = 25

# Calculate the data
gallons_needed = square_feet * paint_needed_per_square_foot
paint_cost = gallons_needed * price_per_gallon
labor_hours = (square_feet / 112) * labor_rate_per_hour
labor_cost = labor_hours
total_cost = paint_cost + labor_cost

# Display results
print("Number of gallons of paint required:", gallons_needed)
print("Cost of the paint: $", paint_cost)
print("Hours of labor required to complete the job:", labor_hours)
print("Cost of the labor to complete the job: $", labor_cost)
print("Total cost of the paint job: $", total_cost)

