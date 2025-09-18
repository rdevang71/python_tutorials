class Car:
    total_cars=0
    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def gereral_description():
        return "Cars are a medium of transport"
    
    @property
    def model(self):
        return self.__model
     
class Battery:
    def battery_info(self):
        return "this is battery"
    
class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar (Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())