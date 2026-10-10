# write a python program to enter P,T,R and calculate compound Interest
P=int(input("Enter Principal amount :"))
R=int(input("Enter Interest Rate :"))
T=int(input("Enter Time in  years :"))

amt=P*(1+R/100)**T

CI=amt-P
print("Compund Interest is :",CI)
