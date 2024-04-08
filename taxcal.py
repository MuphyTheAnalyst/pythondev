#calculating taxes
price=7.5
with_tax= price * 1.09 #9% tax is 1.09
print(price,with_tax)
#print using formaiting expression
print("This uses formating expression to achive the two decimal places")
print("Base Price: ${:.4f}. With Tax: ${:.4f}".format(price,with_tax))

