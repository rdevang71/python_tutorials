class Car:
    total_cars=0
    def __init__(self , brand , model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar (Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_car = Car("Toyota","Corolla")
print(my_car.fuel_type())
# print(my_car.get_brand())


my_tesla = ElectricCar("Tesla","Model S","85kwh")
print(my_tesla.fuel_type())
print(Car.total_cars)