#1 Base class method
class Car:
    def start(self):
        print("Car is starting")

car1 = Car()
car1.start()  #1 Car is starting

#2 Overriding in derived class
class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently")

car2 = ElectricCar()
car2.start()  #2 Electric car is starting silently

#3 Overriding another method
class Car:
    def stop(self):
        print("Car is stopping")

class HybridCar(Car):
    def stop(self):
        print("Hybrid car stops quietly")

car3 = HybridCar()
car3.stop()  #3 Hybrid car stops quietly

#4 Overriding and calling parent method
class Car:
    def honk(self):
        print("Car honks normally")

class SportsCar(Car):
    def honk(self):
        print("Sports car honks loudly")
        super().honk()  # call parent method

car4 = SportsCar()
car4.honk()  #4 Sports car honks loudly, Car honks normally

