array = ["test", "ok","how","why","hello"]
x = []
print ("Given array  {}" .format(array))
x = ([w for w in array if len(w)<4])
print("The words to be removed which are less than 4char are >{}" .format(x))
for w in x:
	array.remove(w)
			
print("new array  {}\n" .format(array))