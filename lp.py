#correcting infinite loops by incrementing the initiliazed variable
#def p_range(start,end):
#	n=start
#	while n <= end:
#		print(n)
#		n +=1
#p_range(1,5)

multi=1
result = multi * 5
while result <=50:
   print(result)
   multi +=1
   result= multi*5
print("Done")
