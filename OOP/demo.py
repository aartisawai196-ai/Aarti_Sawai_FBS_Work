class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
          print(f'id={self.id}\nname={self.name}\nsal={self.sal}')
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getName(self):
            return self.name
    def setName(self,newName):
            self.name=newName
    def getSal(self):
            return self.sal
    def setSal(self,newSal):
            self.id=newSal

e1=Employee(101,'abcd',75687)
e1.display()

