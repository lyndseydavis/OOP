import CarClass as c

car = c.Car("2019", "Land Rover")

print(
    "Start speed of the",
    car.get_year(),
    car.get_model(),
    "is",
    car.get_speed(),
    "mph.",
)
print("I will accelerate the car 5 times.")

for count in range(5):
    car.accelerate()
    print("Current speed: ", car.get_speed(), "mph")

print()
print(
    "Start speed of the",
    car.get_year(),
    car.get_model(),
    "is",
    car.get_speed(),
    "mph.",
)

print("I will brake the car 5 times.")

for count in range(5):
    car.brake()
    print("Current speed: ", car.get_speed(), "mph")
