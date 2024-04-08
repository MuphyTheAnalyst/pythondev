def count_letters(text):
	dictionary= {}
	for char in text.lower():
		if char.isalpha():
			if char not in dictionary:
				dictionary[char]=0
				dictionary[char]+=1
	return dictionary

print(count_letters("AaBbCc"))
print(count_letters("Math is fun! 2+2=4"))

