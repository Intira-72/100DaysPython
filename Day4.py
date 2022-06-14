import random

# Random
random_integer = random.randint(1, 5)
print(random_integer)

random_float = random.random()
print(random_float)

print("-" * 30)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

print("-" * 30)

# List
names = input("Name :").split(", ")
# print(f"{names[random.randint(0, len(names)-1)]} is going to buy the meal today!")
print(f"{random.choice(names)} is going to buy the meal today!")
