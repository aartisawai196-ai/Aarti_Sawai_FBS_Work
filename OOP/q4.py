
class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec

    # def __add__(self, other):
    #     thr=self.hr+other.hr
    #     tmin=self.min+other.min
    #     tsec=self.sec+other.sec
    #     t=Time(thr,tmin,tsec)
    #     return t
    #     # return f"{thr}:{tmin}:{tsec}"
    
    def __sub__(self, other):
        thr=self.hr-other.hr
        tmin=self.min-other.min
        tsec=self.sec-other.sec
        return Time(thr,tmin,tsec)

    def __mul__(self, other):
        thr=self.hr*other.hr
        tmin=self.min*other.min
        tsec=self.sec*other.sec
        return Time(thr,tmin,tsec)

    def __floordiv__(self, other):
        thr=self.hr//other.hr
        tmin=self.min//other.min
        tsec=self.sec//other.sec
        return Time(thr,tmin,tsec)
        
        


    def __add__(self, other):
        tsec=self.sec+other.sec
        cmin=tsec//60
        tmin=self.min+other.min+cmin
        chr=tmin//60
        thr=self.hr+other.hr+chr
        return Time(thr,tmin,tsec)
    


    def __str__(self):
        return f"{self.hr} hr: {self.min} min: {self.sec} sec"

t1=Time(2,45,40)
t2=Time(3,60,7)
t3=t1+t2
print(t3)
print(t1-t2)
print(t1*t2)
print(t1//t2)