# Rectangle class
class Rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.width * self.length)


# Vehicle class
class Vehicle :
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
# Vehicle class without any variables and methods
class Vehicle:
    pass

# Child class Bus that will inherit all of the variables and methods of the Vehicle class 
class Bus(Vehicle):
    pass

