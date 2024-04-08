#using list comprehension
languages=["Python","Perl","Ruby","Go","Java","C"]
lengths=[len(language) for language in languages]
print(lengths)

z=[x for x in range(0,101) if x%3 == 0]
print(z)
