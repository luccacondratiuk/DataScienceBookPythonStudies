list1 = [1,2,3]
list2 = ["a","b","c"]

zipped_list = [pair for pair in zip(list1, list2)]
print(zipped_list)
numbers, letters = zip(*zipped_list)
print(f"Numbers: {numbers}")
print(f"Letters: {letters}")

def add(a: int, b: int) -> int: return a + b

print(f"Function with two integers: {add(1,2)}")
try:
    print(add([1,2]))
except TypeError:
    print("Expecting two integers")
print(f"Function unzipping list of two: {add(1,2)}")
print(add(*[1,2]))

