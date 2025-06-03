### -- The upper() method returns the string in upper case:
a = "Hello, World! -- yoooho"
print(a.upper())

### -- The lower() method returns the string in lower case:

a = "Hello, World! -- yoooho"
print(a.lower())

### -- The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! -- yoooho "
print(a.strip()) # returns "Hello, World!"

### --The replace() method replaces a string with another string:

a = "Hello, World! -- yoooho"
print(a.replace("H", "Z"))
print(a.replace("o", "U"))
print(a.replace("Hello, World! -- yoooho", "Mask of Zorro"))

### -- The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']