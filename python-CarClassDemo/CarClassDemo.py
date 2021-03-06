class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %s MPG."%(self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
my_car.display_car
class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg
    def drive_car(self):
        self.condition = "like new"
        return self.condition
    
my_car = ElectricCar( "molten salt","Luxury", "blue", 120)
print my_car.drive_car()
print my_car.condition 