# write a program to calculate selling price of book based on cost price  and discount
cost_price=int(input("Enter cost price of book"))
dis=int(input("Enter Discount "))

discount=cost_price*dis/100

selling_price=cost_price-discount

print("Selling price of the book is",selling_price)

