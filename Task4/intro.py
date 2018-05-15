str1 = input(str("Enter a sentance > "))
print (str1)
out = str1.split()[0]
intro = ["How", "Why", "What", "Where", "When", "Who"]
if out in intro:
	print (str1 + "?")
else:
	print (str1 + ".")
	
	'''else:
		str1.append(".")
		exit()'''


	

