class Student:
    def __init__(self,id,name,age,per):
        self.id=id
        self.name=name
        self.age=age
        self.per=per

    def __str__(self):
        return f'Student Id :{self.id} \nStudent Name :{self.name} \nStudent Age :{self.age} \nStudent Percentage :{self.per}'

s1=Student(101,'vaishnavi',22,90)
s2=Student(102,'Ashwini',20,95)

print(s1,s2)