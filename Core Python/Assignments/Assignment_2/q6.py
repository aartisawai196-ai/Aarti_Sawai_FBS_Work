# write a program to calculate total salary of employee based on basic, da=10% of basic ta=12% of basic and hra=15% of basic
basic=int(input("Enter Basic salary of employee :"))

da=basic*10/100
Ta=basic*12/100
hra=basic*15/100
print(da,hra,Ta)
total_salary=basic+da+hra+Ta

print("Total salary of employee is :",total_salary)