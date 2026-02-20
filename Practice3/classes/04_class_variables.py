#1 Class variable shared by all cars
class Car:
    color = "red"  # default color for all cars
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("BMW")
print(car1.color)  #red
print(car2.color)  #red

#2 Changing class variable changes all cars
Car.color = "blue"
print(car1.color)  #blue
print(car2.color)  #blue

#3 Instance variable can override class variable
car1.color = "green"
print(car1.color)  #green
print(car2.color)  #blue

#4 Count number of car objects using class variable
class CarCounter:
    count = 0
    def __init__(self, model):
        self.model = model
        CarCounter.count += 1

c1 = CarCounter("Honda")
c2 = CarCounter("Ford")
c3 = CarCounter("Audi")
print(CarCounter.count)  #3 cars
