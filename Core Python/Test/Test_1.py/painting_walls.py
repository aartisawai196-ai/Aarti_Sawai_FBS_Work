area=int(input("Enter area of one wall :"))
interior=int(input("Enter cost of interior wall :"))
exterior=int(input("Enter cost of Exterior wall :"))
interior_cost=6*area*interior
exterior_cost=6*area*exterior
total_cost=interior_cost+exterior_cost
print(f"Total cost is :{total_cost}")