
array = ["test", "ok","how","why","hello"]

print (array)

newword = str(input("Enter that new word to add to the fist postion this array >  "))
print ("New array after inserting word to fist position")
array.insert(0, newword)
print(array)