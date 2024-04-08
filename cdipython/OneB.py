#!/usr/bin/env python3
#Write a program that asks the user to enter the monthly costs for the following
#expenses incurred from operating his or her automobile: loan payment, insurance, gas,
#and maintenance. The program should then display the total monthly costs for these
#expenses and the total annual costs for these expenses. 

# Input expenses
loan_payment = float(input("Enter monthly loan payment: "))
insurance = float(input("Enter monthly insurance cost: "))
gas = float(input("Enter monthly gas cost: "))
maintenance = float(input("Enter monthly maintenance cost: "))

# Calculate total monthly and annual costs
total_monthly_cost = loan_payment + insurance + gas + maintenance
total_annual_cost = total_monthly_cost * 12

# Display results
print("Total monthly automobile expenses: $", total_monthly_cost)
print("Total annual automobile expenses: $", total_annual_cost)

