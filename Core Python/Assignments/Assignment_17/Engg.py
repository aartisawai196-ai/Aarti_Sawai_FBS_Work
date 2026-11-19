class Student:
    def __init__(self,id,name,age,per):
        self.id=id
        self.name=name
        self.age=age
        self.per=per

    def __str__(self):
        return f'Student Id :{self.id} \nStudent Name :{self.name} \nStudent Age :{self.age} \nStudent Percentage :{self.per}'

class Engineers(Student):
    def __init__(self, id, name, age, per,branch,internalMarks):
        super().__init__(id, name, age, per)
        self.branch=branch
        self.internalMarks=internalMarks

    def __str__(self):
        return super().__str__() +f'\nbranch :{self.branch} \nInternal Marks :{self.internalMarks}'


s1=Student(101,'vaishnavi',22,90)
s2=Student(102,'Ashwini',20,95)

e1=Engineers(101,'vaishnavi',22,90,'CS',80)
print(e1)