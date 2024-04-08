#How many times a letter appear in a text
def count_letters(text):
	result={}
	for letter in text:
		if letter not in result:
			result[letter] = 0
		result[letter] += 1
	return print(result)

count_letters("aaaaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")

