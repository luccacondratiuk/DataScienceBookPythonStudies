def double(x:int)->int:
    """
    This is a doc string utilized for describe functions,
    and help (you) and other devs, to understand your code
    This function, return the double of X for example
    """
    return 2*x

def apply_to_one(f):
    """
    In python You can pass a function as parameter
    because you can assign a function to a variable
    And this functions executes the function you passed
    applying 1 as parameter
    """
    return f(1)


double_function = double
x = apply_to_one(double_function)
print(x)

# And you can easily create lambdas too

y = apply_to_one(lambda x: x+4)
print(y)

# Now talking deeper about parameters

def my_print(message:str = "My Custom Default Message")->None:
    """
    Outputs the parameter, if none, outputs
    \"My Custom Default Message\"
    """
    print(message)

my_print("Amazing")
my_print()

# Need named params?
# Easy handle

def construct_full_name(first = "John", last = "Doe")->str:
    """
    Function that Returns a concatenated string
    with a space between the two names
    """
    return first + " " + last

full_name = construct_full_name("Joel", "Grus")
print(full_name)
full_name = construct_full_name("Joel")
print(full_name)
full_name = construct_full_name(last="Joel", first= "Grus")
print(full_name)

