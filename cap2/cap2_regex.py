import re

re_examples = [
    not re.match("a", "cat"),               # Cat doesn't start with an A
    re.search("a","cat"),                   # There is A in cat
    not re.search("c","dogs"),              # There's no C in dogs
    3 == len(re.split("[ab]", "carbs")),    # Splits in a and b, so [c,r,s]
    "R-D-" == re.sub("[0-9]","-","R2D2")    # Substitute numbers by -
]

assert all(re_examples), "All regex examples are true"
