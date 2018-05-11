a = input(str("Write a sentace with deplicate words> "))
str1 = a.split()
out = [] #creating an output array to add non dup words
str2 = set() #creating a set fun to eliminating duplicate
print (str1)
for word in str1:
	if word not in str2: #words comparing with set() string
		out.append(word) 
		str2.add(word) #appending words after each iteration
out.sort()# sorting happens over here

print ("Sorted sentance without duplication")
print (' '.join(out))