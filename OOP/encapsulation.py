#write a program to perform encapsulation

class Player:
    def __init__(self,jrno,name,matches):
        self.jrno=jrno
        self.name=name
        self.matches=matches
    def display(self):
        print(f"jrno={self.jrno}  name={self.name} matches={self.matches}")


p1=Player(101,'virat','abc')
p1.display()