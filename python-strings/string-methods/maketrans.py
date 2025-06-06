### -- Create a mapping table, 
### --  and use it in the translate() method to replace any "S" characters with a "P" character:

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

### ASCII translation

### -- use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
