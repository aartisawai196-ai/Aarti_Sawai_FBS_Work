class Ticket:
    def __init__(self,id,price):
        self.id=id
        self.price=price
    def display(self):
        print(f'id={self.id}\n price={self.price}')
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getPrice(self):
            return self.price
    def setPrice(self,newPrice):
            self.price=newPrice

e1=Ticket(102,500)
e2=Ticket(106,800)
e1.display()
e1.setId(101)
e1.display()
e2.display()
e2.setPrice(9000)
e2.display()