from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def __str__(self):
        return f"name={self.brand} color={self.color}"
    @abstractmethod
    def brake(self):
        pass
class car(Vehicle):
    def __init__(self, brand, color,sunroof):
        super().__init__(brand, color)
        self.issunroof=sunroof
    def __str__(self):
        return super().__str__()+f'sunroof available {self.sunroof}'
    def brake(self):
        print("drump brake of car")

v1=Vehicle('Mahindra','white')
v1.brake()
c1=car('Mahindra','White','yes')
c1.brake()