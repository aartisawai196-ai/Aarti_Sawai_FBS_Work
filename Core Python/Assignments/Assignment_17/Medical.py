class Student:
    def __init__(self,id,name,age,per):
        self.id=id
        self.name=name
        self.age=age
        self.per=per

    def getId(self):
        print(self.id)

    def setId(self,newId):
        self.id=newId

    def getName(self):
            print(self.name)
    
    def setName(self,newName):
            self.id=newName

    def getAge(self):
            print(self.age)
    
    def setAge(self,newAge):
            self.id=newAge

    def getPer(self):
            print(self.per)
    
    def setPer(self,newPer):
            self.id=newPer
        

    def __str__(self):
        return f'Student Id :{self.id} \nStudent Name :{self.name} \nStudent Age :{self.age} \nStudent Percentage :{self.per}'

class Medical(Student):
    def __init__(self, id, name, age, per,specialization,InternshipMarks):
        super().__init__(id, name, age, per)
        self.specialization=specialization
        self.InternshipMarks=InternshipMarks

    def __str__(self):
        return super().__str__() +f'\nSpecialization :{self.specialization} \nMarks Of Internship :{self.InternshipMarks}'


s1=Student(101,'vaishnavi',22,90)
s2=Student(102,'Ashwini',20,95)

m1=Medical(101,'vaishnavi',22,90,'Botony',80)
print(m1)