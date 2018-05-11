array = ["test", "ok","how","why","hello"]

print (array)

newword = str(input("Enter that new word to add to the last postion this array >  "))
print ("New array after inserting word to fist position")
array.insert(len(array), newword)
print(array)