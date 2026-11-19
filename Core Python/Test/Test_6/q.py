from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,noofperson):
        self.noofperson=noofperson

    def __str__(self):
        return f'No of persons{self.noofperson}'

    @abstractmethod
    def cal_toll():
        pass
    

class TwoWheeler(Vehicle):
        
    def cal_toll(self):
        toll=20

        if self.noofperson>2:
            toll+=(self.noofperson-2)*10

        print(f'Toll for two Wheeler is{toll}')

class ThreeWheeler(Vehicle):
        
    def cal_toll(self):
        toll=30

        if self.noofperson>3:
            toll+=(self.noofperson-3)*20

        print(f'Toll for Three Wheeler is{toll}')
        

class FourWheeler(Vehicle):
        
    def cal_toll(self):
        toll=40

        if self.noofperson>4:
            toll+=(self.noofperson-4)*40

        print(f'Toll for Four Wheeler is{toll}')
        

class HeavyVehicle(Vehicle):
        
    def cal_toll(self):
        toll=100

        if self.noofperson>6:
            toll+=(self.noofperson-6)*10

        print(f'Toll for Heavy Vehicle is {toll}')
        
        
        
t1=TwoWheeler(3)
t2=ThreeWheeler(4)
t3=FourWheeler(5)
t4=HeavyVehicle(7)

print(t1,t2,t3,t4)
t1.cal_toll()
t2.cal_toll()
t3.cal_toll()
t4.cal_toll()
