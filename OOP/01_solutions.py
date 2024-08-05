class Car:
    total_cars = 0 #this is a class variable 

    def __init__(self, brand, model):
        self.__brand = brand # ENCAPSULATION. the 2 underscore in front of 'brand' made it a private variable
        self.__model = model  #self.model is the attribute for class 'Car' & the 2nd 'model' is the parameter for the function '__init__'
        Car.total_cars += 1    #this will keep track of how many OBJECTS are made. Even the OBJECTS made by child class will be counted.
        # this works because everytime an OBJECT is made, be it parent or child class, the function '__init__' is always called first.

    def get_brand(self): #Since brand is private we can use this to access brand
        return self.__brand

    def set_brand(self, new_brand):#Since brand is private we can use this to change value of brand
        self.__brand = new_brand

    def fuel_type(self):     #POLYMORPHISM. Parent and Child class have same named methods with different behaviours
        return "Petrol or Diesel"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    # '@anything' is called DECORATORS.

    @staticmethod       #this is how to declare a STATIC METHOD 
    def description():  #no need to write self here because objects are NOT MEANT to access this.
        return "Cars are amazing"   #Can only be accessed by 'Car'

    @property   #Makes sure that '__model' cannot be accessed or over-written without this method.
    def model(self):        #the property decorator also helps '__model' to be accessed just like an attribute instead of a function.
        return self.__model #Meaning, you dont need to do 'my_car.model()'. Instead just 'my_car.model' works fine.

class ElectricCar(Car):         #INHERITENCE
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):        #POLYMORPHISM. Parent and Child class have same named methods with different behaviours
        return "Electricity"



my_car = Car("Masda", "Miata")
# print(my_car.__brand) # Cannot access beacause brand is private.
# print(my_car.model)
# print(my_car.full_name())
# print("Brand:",my_car.get_brand())
# my_car.set_brand("Luffy")
# print("New Brand:",my_car.get_brand())
# print("Full name:",my_car.full_name())
# print("Fuel:",my_car.fuel_type())

# print(isinstance(my_car, Car))          # checks if 'my_car' is an instance/OBJECT of the class 'Car'
# print(isinstance(my_car, ElectricCar))  # checks if 'my_car' is an instance/OBJECT of the class 'ElectricCar'


    
my_electric_car = ElectricCar("Tesla", "Model X", "105 kWh")
# print(my_electric_car.__brand)    # Cannot access beacause brand is private.
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
# print(my_electric_car.full_name())
# print("Brand:",my_electric_car.get_brand())
# my_electric_car.set_brand("Jojono")
# print("New Brand:",my_electric_car.get_brand())
# print("Full Name:",my_electric_car.full_name())
# print("Fuel:",my_electric_car.fuel_type())

# print(isinstance(my_electric_car, Car))         # checks if 'my_electric_car' is an instance/OBJECT of the class 'Car'
# print(isinstance(my_electric_car, ElectricCar)) # checks if 'my_electric_car' is an instance/OBJECT of the class 'ElectricCar'


# print(Car.total_cars)   #You can directly access the class variable like this.

# print(Car.description())    #Any objects trying to access 'description()' will give an error. this is the only way to access a static method


# MULTIPLE INHERITENCE
class Battery:
    def battery_info(self):
        return "this is a battery"

class Engine:
    def engine_info(self):
        return "this is an enigine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_tesla = ElectricCar2("Tesla", "Model S")
# print(my_tesla.battery_info())
# print(my_tesla.engine_info())