def generate_range(n = 1):
    i = 0
    while i < n:
        yield i
        i+=1

def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


for i in generate_range(10):
    print(f"i = {i}")

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_6 = (x for x in even_squares if x % 10 == 6)
# all these generators do nothing until you iterate
# it's like creating a pipeline for data processing

names = ["John", "Alice", "Bob", "Charlie"]
for i , name in enumerate(names):
    print(f"Index: {i} -> name: {name}")

