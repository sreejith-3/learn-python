"""
Search for the last occurrence of the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
"""
"""
partition(sep)
Splits the string at the first occurrence of the specified separator (sep).

Returns a tuple of 3 parts: (before, separator, after).

rpartition(sep)
Splits the string at the last occurrence of the specified separator.

Also returns a tuple of 3 parts: (before, separator, after).
"""
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)rpartition.