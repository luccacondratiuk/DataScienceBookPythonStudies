## How to handle errors in runtime, without breaking everything

number = 0
try:
    print(number/number)
except ZeroDivisionError:
    print("Cannot divide by zero, almost like an hacker attack")