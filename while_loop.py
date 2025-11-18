num = int(input("Please enter a number"))


count = 0
temp = num

# If the number is 0, it has 1 digit
if temp == 0:
    count = 1
else:
    while temp != 0:
        temp = temp // 10   # Remove the last digit
        count += 1          # Count it

print("Number of digits:", count)

