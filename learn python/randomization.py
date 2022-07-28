import random
random_int = random.randint(5,30)
print(random_int)
# to print a random float num
random_float = random.random()
print(random_float)
fruit = [ 'mango','pineapple','cashew','guava','orange']
print(random.choice(fruit))
random.shuffle(fruit)
print(fruit)