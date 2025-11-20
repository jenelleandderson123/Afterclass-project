num = int(input("Enter a decimal number: "))
n = num  
binary = ""


while num > 0:
    remainder = num % 2
    for _ in range(1):
        binary = str(remainder) + binary
    
    num = num // 2

print("Binary of", n, "is:", binary)
