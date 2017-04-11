import car
# 此时用句号表示法访问car.***
# from car import *  直接访问即可
# from car import Car, ElectricCar

my_new_car = car.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 30
my_new_car.update_odometer(110)
my_new_car.read_odometer()
my_new_car.update_odometer(100)
my_new_car.increment_odometer(-20.5)
my_new_car.read_odometer()

my_tesla = car.ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
