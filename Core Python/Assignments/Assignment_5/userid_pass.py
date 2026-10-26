#write a program to prompt user to enter userid and password if id and and password is incorrect giv him
#chance to re-enter the credential let hime try 3 times after that program to terminate

userid=int(input("Enter userid :"))
password=int(input("Enter password :"))

uid=101
pwd=123456
chance=1
if(userid!=uid and password!=pwd):
    while chance!=4:
        print("Please re-enter credential !!")
        userid=int(input("Enter userid :"))
        password=int(input("Enter password :"))
        chance+=1
else:
    print("Valid credentials!")

