### -- Where in the text is the last occurrence of the string "casa"?:
### rfind() : Search for a substring from the right (end of the string).
### rindex() :  Return the highest index (last occurrence) where the substring is found.

"""
Key difference :
Method	       If substring is found	             If substring is not found
rfind()	         Returns index	                            Returns -1
rindex()	     Returns index	                            Raises ValueError
"""

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)