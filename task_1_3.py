price = float(input("Enter a price of a product: "))
quantity = int(input("Enter a quantity of a product: "))

total_price = price * quantity

discount_price = total_price * 0.85

print("Total price:", total_price)
print()
print("Price after 15% discount:", discount_price)
