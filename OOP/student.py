class student:
    def __init__(self,frn,name,batch,iname):
        self.frn=frn
        self.name=name
        self.batch=batch
        self.iname=iname
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
    def getiname(self):
            return self.iname
    def setiname(self,newiname):
            self.iname=newiname
    def display(self):
        print(f'frn={self.frn}\n name={self.name}\n batch={self.batch}\n iname={self.iname} ')
    def __del__(self):
          print("I am destructor ")
          print(self.name)
          self.frn=None
          self.name=None
          self.batch=None
          self.iname=None
          print(self.name)
s1=student(101,'abc','sep python','FBS')
s2=student(102,'xyz','aug python','FBS')
s3=student(103,'pqr','july python','FBS')
s1.display()
s1.setname("aarti")
s1.display()
s2.display()
s3.display()
    
        