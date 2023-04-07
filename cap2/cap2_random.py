import random
random.seed(10)

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)
#print always the same numbers, because we defined a seed

print(random.randrange(10))         # Selecting a random number in the range 0-10
print(random.randrange(3,6))        # Selecting a random number in the range 3-6

up_to_ten = list(range(1,11))
print(up_to_ten)
random.shuffle(up_to_ten)
print(up_to_ten)                    # Note that how we set a seed, result always the same

print(random.choice(up_to_ten))     # Selecting random element from the provided list
print(random.sample(up_to_ten, 3))  # Selecting 3 random elements from the provided list
