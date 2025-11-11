# Taking units

units = int(input("Please enter the amount of electricity you have consumed:"))

if(units) < 50:
    amount = units * 2.60
    charge = 25
elif(units <= 100):
    amount = 130 +((units - 50) * 3.25)
    charge = 35
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100)* 5.26)
    charge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200))
    charge = 75

# calculating and show the total

total = amount + charge
print("\n Electricity Bill = %.2f" %total)