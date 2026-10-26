#enter number of student from user for those many students accept marks of 5 subject marks from user and calculate
#percentage of students. Display all percentage and average percentage of 

no_of_students=int(input("Enter no of students ::"))
i=1
sum=0
avg=0
while i<no_of_students+1:
    m1=int(input("Enter marks 1 :"))
    m2=int(input("Enter marks 2 :"))
    m3=int(input("Enter marks 3 :"))
    m4=int(input("Enter marks 4 :"))
    m5=int(input("Enter marks 5 :"))

    per=(m1+m2+m3+m4+m5)/5
    print(f"percentage of student {i} is {per}")
    sum+=per
    i+=1

avg=sum/no_of_students
print(f'average of {no_of_students} is {avg}')

    
