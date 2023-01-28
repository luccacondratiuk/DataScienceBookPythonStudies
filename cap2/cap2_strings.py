# There's to ways of handling strings in python
# Single quoted
single_quoted = 'Single Quotes'
# and Double quoted
double_quoted = "Double Quotes"

# If you want to use Special Characters, use \ character
tab_string = "\t"
# the length of this variable is not 2,
# because is not \ and t, it's only tab character
print(tab_string)
print(len(tab_string))

# For raw Strings, just utilize r""
raw_string = r"\t"
print(raw_string)
print(len(raw_string))

# For multiline Strings:
multiline_string = """First line
Second Line
Third Line"""
print(multiline_string)

# Now let's start using powers
# For python >=3.6, we can use the famous f-strings
# See the magic
first_name = "John"
last_name = "Doe"
# Ancient way
full_name = first_name + " " + last_name
print(full_name)
# Old way
full_name = "{0} {1}".format(first_name, last_name)
print(full_name)
# Present way
full_name = f"{first_name} {last_name}"
print(full_name)
