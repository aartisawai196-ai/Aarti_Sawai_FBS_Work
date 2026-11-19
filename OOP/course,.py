class Course:
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
    def display(self):
        print(f'name={self.name}\n Duration={self.duration}')
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getDuration(self):
            return self.duration
    def setDuration(self,newDuration):
            self.duration=newDuration

e1=Course('Data Science',5)
e2=Course('Full stack',10)

e1.display()
e1.setName('Data Analytics')
e1.display()

e2.display()
e2.setDuration(7)
e2.display()