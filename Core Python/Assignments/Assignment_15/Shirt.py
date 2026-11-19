class Shirt:
    def __init__(self,sid,sname,price,size):
        self.sid=sid
        self.sname=sname
        self.price=price
        self.size=size

    def ShowShirt(self):

        print(f'Shirt Id :{self.sid}')
        print(f'Shirt Name :{self.sname}')
        print(f'Shirt Price :{self.price}')
        print(f'Shirt Size :{self.size}')
        print("\n")


    def __del__(self):

        self.sid=None
        self.sname=None
        self.price=None
        self.size=None


s1=Shirt(101,'Formal',500,'Medium')
s2=Shirt(102,'Semi-Formal',900,'small')

s1.ShowShirt()
s2.ShowShirt()