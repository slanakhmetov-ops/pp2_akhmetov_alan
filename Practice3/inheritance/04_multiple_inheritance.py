#1 Simple multiple inheritance
class Engine:
    def engine_type(self):
        print("Gas engine")

class Wheels:
    def wheels_info(self):
        print("4 wheels")

class Car(Engine, Wheels):
    pass

car1 = Car()
car1.engine_type()  #1 Gas engine
car1.wheels_info()  #1 4 wheels

#2 Overriding method in child
class ElectricCar(Engine, Wheels):
    def engine_type(self):
        print("Electric engine")

car2 = ElectricCar()
car2.engine_type()  #2 Electric engine
car2.wheels_info()  #2 4 wheels

#3 Adding new method in child
class HybridCar(Engine, Wheels):
    def fuel_info(self):
        print("Hybrid fuel")

car3 = HybridCar()
car3.engine_type()  #3 Gas engine
car3.fuel_info()    #3 Hybrid fuel

#4 Overriding and calling parent method
class SportsCar(Engine, Wheels):
    def engine_type(self):
        print("Turbo engine")
        super().engine_type()

car4 = SportsCar()
car4.engine_type()  #4 Turbo engine, Gas engine
car4.wheels_info()  #4 4 wheels