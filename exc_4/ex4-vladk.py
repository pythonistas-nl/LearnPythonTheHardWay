#number of cars
cars = 100
#spaces in a car
spaces_in_a_car = 4
#drivers 
drivers = 30
#passengers
passengers = 90
#cars not driven
cars_not_driven = cars - drivers
#cars driven
cars_driven = drivers
carpool_capacity = cars_driven * spaces_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars too.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")	