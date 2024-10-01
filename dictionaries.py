# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals)) # Description
# print(help(capitals))
print(capitals.get("USA"))
print(capitals.get("Japan")) # This command get's you "None"

if capitals.get("Japan"):
    print("That capital exists")
else: 
    print("That capital doesn't exist")

if capitals.get("India"):
    print("That capital exists")
else: 
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) # Adds value
capitals.update({"USA": "Detriot"}) # Changes existing value
capitals.pop("China") # Pops out the value
capitals.popitem() # Pops out the latest value

# capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
    
print(capitals)