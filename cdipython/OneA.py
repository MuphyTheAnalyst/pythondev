#!/usr/bin/env python3
#Assume hot dogs come in packages of 10, and hotdog buns come in packages of 8. Write
#a program that calculates the number of packages of hot dogs and the number of
#packages of hot dog buns needed for a cookout, with minimum amount of leftovers. The
#program should ask the user for the number of people attending the cookout and the
#number of hot dogs each person will be given. The program should display the following
#details:
#   The minimum number of packages of hot dogs required.
# The minimum number of packages of hot dog buns required
# The number of hot dogs that will be left over
# The number of hot dog buns that will be left over

# Input from the user
num_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Constants
hot_dogs_per_package = 10
buns_per_package = 8

# Calculate the required packages
hot_dog_packages = num_people * hot_dogs_per_person / hot_dogs_per_package
bun_packages = num_people * hot_dogs_per_person / buns_per_package

# Calculate leftovers
hot_dogs_leftover = hot_dog_packages * hot_dogs_per_package - num_people * hot_dogs_per_person
buns_leftover = bun_packages * buns_per_package - num_people * hot_dogs_per_person

# Display results
print("Minimum number of packages of hot dogs required:", int(hot_dog_packages))
print("Minimum number of packages of hot dog buns required:", int(bun_packages))
print("Number of hot dogs that will be left over:", hot_dogs_leftover)
print("Number of hot dog buns that will be left over:", buns_leftover)


