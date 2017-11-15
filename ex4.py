
print()

# define cars variables
cars = 100
# define space_in_a_car
space_in_a_car = 4.0
# define drivers
drivers = 30
# define passengers
passengers = 90
# define cars_not_driven
cars_not_driven = cars - drivers
# define cars_driven
cars_driven = drivers
# define carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# define average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# print how many cars there are
print("There are", cars, "cars available.")

# print how many drivers are available
print("There are only", drivers, "drivers available.")

# calculate and print how many empty cars there are.
print("There will be", cars_not_driven, "empty cars today.")

# calc and print carpool_capacity
print("We can transport", carpool_capacity, "people today.")

# calc and print no. of passengers available
print("We have", passengers, "to carpool today.")

# summarize how many passengers needed in each cars
print("We need to put about", average_passengers_per_car, "in each car.")
