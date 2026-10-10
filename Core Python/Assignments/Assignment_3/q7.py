# write a program to check if user has entered correct userid and password
userid=input("Enter userid :")
password=input("Enter Password :")

uid="aarti"
pwd="123"

if(userid==uid and password==pwd):
    print("Both are correct")
elif(userid!=uid):
    print("Wrong Username.")
else:
    print("Wrong Password.")
