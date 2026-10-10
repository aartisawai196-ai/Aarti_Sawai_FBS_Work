gender=input("Enter genger(F/M)")
age=int(input("Enter Age:"))

if (gender=='F'):
    if(age>=18):
        print("Eligible for marriage..!!")
    else:
        print("Not Eligible for marriage...!")
else:
    if(age >=21):
        print("Eligible for Marraiage...!")
    else:
        print("Not eligible for marriage..!")