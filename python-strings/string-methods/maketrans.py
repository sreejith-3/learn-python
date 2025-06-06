### -- Create a mapping table, 
### --  and use it in the translate() method to replace any "S" characters with a "P" character:

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))