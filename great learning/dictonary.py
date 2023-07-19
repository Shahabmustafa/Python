fruit = {"Apple" : 10,"Banana" : 20,"Orange" : 30,"Mango" : 40}

print(type(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit.items())
fruit["peach"] = 50
fruit["Apple"] = 20
fruit.pop("Apple")
print(fruit)