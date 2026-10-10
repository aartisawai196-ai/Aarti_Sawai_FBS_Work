gender=input("Enter gender (M/F)")
age=int(input("Enter age :"))

if(gender=='F'):
    if(age>=18):
        print("Eligible")
    else:
        print("Not Eligible")
else:
    if(age>=21):
        print("Eligible")
    else:
        print("Not eligible")