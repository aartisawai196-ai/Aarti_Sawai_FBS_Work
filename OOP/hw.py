class student:
    scount=0
    def __init__(self,frn,name,batch):
        self.frn=frn
        self.name=name
        self.batch=batch
        student.scount+=1

    def getFrn(self):
        return self.frn
    def setFrn(self,newfrn):
        self.frn=newfrn
    def getname(self):
            return self.name
    def setFrn(self,newname):
            self.name=newname
    def getbatch(self):
            return self.batch
    def setbatch(self,newbatch):
            self.batch=newbatch
    def display(self):
          print(f"frn id={self.frn} name={self.name} batch={self.batch}")

class PlacedStudent(student):
      def __init__(self, frn, name, batch, cname):
            super().__init__(frn, name, batch)
            self.cname=cname
      def setcname(self):
                  return self.cname
      def getcname(self,newcname):
                  self.cname=newcname

      def display(self):
              super().display()
              print(f"company name={self.cname}")
              
      

s1=student(101,'Ram','aug')
p1=PlacedStudent(102,'shyam','sep','cognizant')
p1.display()

print(student.scount)