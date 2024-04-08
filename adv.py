#using curly bracket {} and format method
name="Manny"
number =len(name)*3
print("Hello {}, your lucky number is {}".format(name,number))
# insert the values of each variables to use it in the format
print("Hello {number}, your lucky name is {name}".format(name=name,number=len(name)*3))


def stud_grade(names,grade):
	return "{} received {}% on the exam".format(names,grade)
print (stud_grade("Reed",80))
print (stud_grade("Paife",92))
print (stud_grade("Jesse",85))
