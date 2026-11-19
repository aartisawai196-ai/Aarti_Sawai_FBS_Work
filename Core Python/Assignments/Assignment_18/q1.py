class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self, other):
        r=self.real+other.real
        i=self.img+other.img
        return Complex(r,i)

    def __sub__(self, other):
        r=self.real-other.real
        i=self.img-other.img
        return Complex(r,i)

    def __str__(self):
        return f'real:{self.real} img:{self.img}'

    def __del__(self):
        self.real=None
        self.img=None
        print(f'real={self.real} img={self.img}')
c1=Complex(2,9j)
c2=Complex(4,6j)
res=c1+c2
print(res)
print(c1-c2)