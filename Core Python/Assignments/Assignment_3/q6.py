# write a program to calculate profit or loss
selling_price=int(input("Enter selling price :"))
cost_price=int(input("Enter Cost price"))

profit=selling_price-cost_price
loss=cost_price-selling_price
if (selling_price>cost_price):
    print("Profit is :",profit)
else:
    print("Loss is :",loss)