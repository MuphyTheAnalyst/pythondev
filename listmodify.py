fruits=["Orange","Banana","Apple"]
fruits.append("Kiwi")
print (fruits)


fruit=["Nuts","Apple","Banana"]
fruit.insert(2,"Grapes")
print(fruit)


#using tuples to get email format and using enumerate function
winners=["Ashely","Dylan","Doug"]
for index,person in enumerate(winners):
	print("{} - {}".format(index+1,person))

