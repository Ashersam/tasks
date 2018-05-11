a = input(str("Write a sentace> "))
a = a.lower()
str1 = a.split(' ')
print (str1)

str2 = (sorted(set(str1), key=str1.index))
str2.sort()
print (str2)
