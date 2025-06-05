### -- Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "For only {price:.5f} dollars!"
print(txt.format(price = 49))