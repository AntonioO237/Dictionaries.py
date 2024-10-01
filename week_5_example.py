cars = ["bmw", "maserati", "audi", "mercedes", "ferrari"]
print(f"thse are list of {cars}")
print(f"the first cas is {cars[0]}")
# Changing the value of the list
cars[0] = "toyota"
print(f"the first cas is {cars[0]}")
print(f"the last car is {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")
#adding a new value to the list
cars.append("bugatti")
print(cars)
cars.remove("maserati")
print(cars)
# Looping through the list
# Otherwise called iterating through the list 
for car in cars:
    # print(len(car))
    # print(car)
    carRequest = input("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)