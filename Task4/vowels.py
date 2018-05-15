read_file  = open('file.txt', 'r')
file = read_file.read()
str1 = file.split(' ')
out=[]
print (str1)
vowels=['a','e','i','o','u','A','E','I','O','U']
for letter in str1:
	for x in letter:
		if x in vowels:
			out.append(letter.strip('\n'))
			str2 = (sorted(set(out), key=out.index))
print(str2)


