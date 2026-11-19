class Payment:
    def __init__(self,amount,date):
        self.amount=amount
        self.date=date
    def display(self):
        print(f'amount={self.amount}\n date={self.date}')
    def getAmount(self):
        return self.amount
    def setAmount(self,newAmount):
        self.amount=newAmount
    def getDate(self):
            return self.date
    def setDate(self,newDate):
            self.date=newDate

e1=Payment(90000000,'13-08-2027')
e1.display()
e2=Payment(60000,'6-8-2045')
e1.setAmount(800000)
e1.display()
e2.display()
e2.setDate('1-1-2001')
e2.display()



        