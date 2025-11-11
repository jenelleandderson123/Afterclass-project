num = float(input("Enter a number: "))

if num < 0:
    print("Square root of a negative?? Be serious. This is basic math, not wizard school.")
else:
    sqrt = num ** 0.5
    print("The square root of", num, "is", sqrt)
