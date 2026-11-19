class student:
    iname="Firstbit solutions"
    def __init__(self,frn,name,batch):
        self.frn=frn
        self.name=name
        self.batch=batch
    def getFrn(self):
        return self.frn
    def setFrn(self,newfrn):
        self.frn=newfrn
    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname
    def getbatch(self):
            return self.batch
    def setbatch(self,newbatch):
            self.batch=newbatch
    @staticmethod
    def login():
          print("I'm from static method")
    def display(self):
        print(f'frn={self.frn}\n name={self.name}\n batch={self.batch}\n iname={self.iname} ')
    
s1=student(101,'abc','sep python')
s1.display()
student.login()
s1.login()

        