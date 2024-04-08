#To print the sum of the areas of two triangles using functions
def area_triangle(base,height):
	return base*height/2
#intentionally left black
area_1= area_triangle(5,4)
area_2 = area_triangle(7,3)
sum =area_1 + area_2
print("The sum of both areas is: " + str(sum))

