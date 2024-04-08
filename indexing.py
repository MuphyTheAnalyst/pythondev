#indexing
color="Orange"
print(color[1:4])

fruit='Pineapple'
print(fruit[:4])
print(fruit[4:])

#change a wrong type
message="A kong string with a silly typo"
#change k to l
new_message=message[0:2] + "l" +message[3:]
print (new_message)


pets="Cats & Dogs"
print(pets.index("&"))
print(pets.index("D"))
