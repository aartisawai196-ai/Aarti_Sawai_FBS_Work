import random
uid="aarti"
password="123"
userid=input("Enter userid")
pwd=input("Enter password")

if(userid==uid and password==pwd):
    rno=random.randint(1000,9999)
    print(rno)
    uno=int(input("Enter captcha."))
    if(rno==uno):
        print("Success")
    else:
        print("Invalid Captcha")
else:
    print("wrong username and password")


