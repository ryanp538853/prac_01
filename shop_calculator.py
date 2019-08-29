total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of Items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of items: "))
    total = total + price

if total > 100:
    total = total * 0.9

print("Total price for", number_of_items, "items is $", total)
