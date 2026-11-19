class Distance:
    def __init__(self,km,mm,cm):
        self.km=km
        self.mm=mm
        self.cm=cm

    def __str__(self):
        return f'Kilometer :{self.km} Meter: {self.mm} Centimeter{self.cm}'

    def __add__(self, other):
        tkm=self.km+other.km
        tmm=self.mm+other.mm
        tcm=self.cm+other.cm
        return Distance(tkm,tmm,tcm)

    def __sub__(self, other):
            tkm=self.km-other.km
            tmm=self.mm-other.mm
            tcm=self.cm-other.cm
            return Distance(tkm,tmm,tcm)

    def __del__(self):
         self.km=None
         self.mm=None
         self.cm=None
         print(f'{self.km}{self.mm}{self.cm}')


d1=Distance(24,12,10)
d2=Distance(12,6,5)

# print(d1,d2)
print(d1+d2)
print(d1-d2)
