class Deilvery:
    def __init__(self,id,addr):
        self.id=id
        self.addr=addr
    def display(self):
        print(f'id={self.id}\n address={self.addr}')
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getAddr(self):
            return self.addr
    def setAddr(self,newAdrr):
            self.addr=newAdrr

e1=Deilvery(1,'pune')
e2=Deilvery(2,'Mumbai')
e1.display()
e1.setId(3)
e1.display()
e2.display()
e2.setAddr('chh sambhajinagar')
e2.display()