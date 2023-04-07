# So what if we create a function, that receives as parameter a function,
# and returns two times the value of the parameter function for any entry
# Confused? Me too, let's try to implement and see if it's useful

def doubler(f):
    def g(x: int)-> int:
        return 2 * f(x)

    return g

def f1(x: int) -> int:
    return x + 1

print(f"F1 pure result, for x = 3: {f1(3)}")
f2 = doubler(f1)
print(f"F2 (double F1), for x = 3: {f2(3)}")

# but it doesn't work for more parameters

def f3(x:int, y:int) -> int:
    return x + y
f2 = doubler(f3)
try:
    print(f2(1,2))
except TypeError:
    print("Only one argument as defined")

# But with unzipping and some black magic, we can do something:

def magic(*args, **kwargs)->None:
    print(f"Unnamed Arguments: {args}")
    print(f"Named Arguments: {kwargs}")

magic(1,2, key="word1", key2="word2")

def more_weird_magic(x:int,y:int,z:int)->int:
    return x + y + z

x_y_list = [1,2]
z_dict = {"z" : 3}
print(f"Magic of disorder: {more_weird_magic(*x_y_list,**z_dict)}")

# So the "correct" way of the doubler should be:

def correct_doubler(f):
    def g(*args, **kwargs):
        return 2*f(*args,**kwargs)
    return g

f2 = correct_doubler(f3)
print(f"F3 alone: {f3(1,2)}")
print(f"Correct doubler (F3): {f2(1,2)}")
