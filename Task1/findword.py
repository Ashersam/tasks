
def wordfind():

	line = str(input("Write a sentance> "))
	#text = line.split()

	#print(text)

	new_string = ' '.join([w for w in line.split() if len(w)<4])
	print ("those words which is less than 4 char are\n ",new_string)

wordfind()
