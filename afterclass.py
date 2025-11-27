rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # spaces first to push the stars to the right
    print(" " * (rows - i) + "*" * i)
