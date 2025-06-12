### -- For loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


### -- You can also loop through the list items by referring to their index number.
### -- Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

## -- A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]