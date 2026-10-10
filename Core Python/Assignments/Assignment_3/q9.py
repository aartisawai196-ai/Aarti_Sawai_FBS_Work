m1=int(input("Enter Marks of subject 1:"))
m2=int(input("Enter Marks of subject 2:"))
m3=int(input("Enter Marks of subject 3:"))
m4=int(input("Enter Marks of subject 4:"))
m5=int(input("Enter Marks of subject 5:"))

total=m1+m2+m3+m4+m5
per=total/5

if(per>=90):
    print("First Class")
elif(per>=70 and per<=80):
    print("second class")
elif(per>70 and per<=50):
    print("Third Class")
elif(per<50 and per>=35):
    print("Need More study")
else:
    print("FAIL")