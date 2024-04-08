#demonstrate branching
def hint_username(username):
	if len(username) < 3:
		print("Invalid username. Must be at least 3 characters long")
	elif len(username) > 15: 
		print("Too Long username.")
	else:
		print ("username is ok")

hint_username("olajideusmancomehomewithme")

#function to determine if a number is even
def is_even(number):
	if number % 2 == 0:
		print("True")
	else: 
		print("false")

is_even(2)

