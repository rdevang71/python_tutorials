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
    
class ElectricCar (Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_tesla = ElectricCar("Tesla","Model S","85 kwh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))