age = int(input("Enter the age"))
day = str(input("Enter the day"))

price = 12 if age>=18 else 8
price = (price-2) if day=="Wednesday" else price

print("Your ticket price is $",price)