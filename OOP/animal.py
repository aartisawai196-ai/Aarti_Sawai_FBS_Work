class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'name={self.name}\n age={self.age}')
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getAge(self):
            return self.age
    def setAge(self,newAge):
            self.age=newAge

e1=Animal('cat',5)
e2=Animal('Dog',10)
e1.display()
e1.setName("cowww")
e1.display()
e2.display()
e2.setAge(7)
e2.display()