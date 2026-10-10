# write a program to convert days into years weeks and days
days=int(input("Enter days :"))
year=days//365
rem_days=days%365

weeks=rem_days//7
remaining_days=rem_days%7

print("Year is :",year,"year")
print("Weeks are :",weeks,"weeks")
print("Days are :",remaining_days,"days")
