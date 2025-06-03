### As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

### But we can combine strings and numbers by using f-strings or the format() method!

age = 36
txt = f"My name is John, I am {age}"
print(txt)

### A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)

## Display the price with 2 decimals:

price = 39
txt = f"The price is {price:.2f} dollars"
print(txt)

## Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars -woo"
print(txt)