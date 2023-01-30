# A list of integer elements
integer_list = [1,2,3,4,5]

# A list of wtf elements
# Yes you can do this mess, but should you? You tell me...
mess_list = ['String', 1.2, True, 2]

# A list of lists
# I won say a word about this...
list_of_list = [[], integer_list, mess_list]

# Some useful functions 
list_length = len(integer_list) # yeah I know, it could be a list method...
list_sum = sum(integer_list) # be careful 
print(list_length)
print(list_sum)

# Using this ->[]
x = [0,1,2,3,4,5,6,7,8,9]
zero = x[0]     # First element of list is 0 index
nine = x[-1]    # Last element
eight = x[-2]   # May be useful, but please, keep it simple
x[0] = -1       # now x = [-1,1,2,3,4,5,6,7,8,9]

# List Slicing
first_three_elements = x[:3]        # [-1,1,2]
three_to_end_elements = x[3:]       # [3,4,5,6,7,8,9]
one_to_four = x[1:5]                # [1,2,3,4]
last_three_elements = x[-3:]        # [7,8,9]
without_first_and_last = x[1:-1]    # [1,2,3,4,5,6,7,8]
copy_of_x = x[:]                    # [-1,1,2,3,4,5,6,7,8,9]
# You can put another argument, that work like a stride/step
every_third = x[::3]                # [-1,3,6,9]
five_to_three = x[5:2:-1]           # [5,4,3]

# Operands
print(1 in [1,2,3]) # True
print(0 in [1,2,3]) # False

x = [1,2,3]
x.extend([4,5,6])
print(x)
x = x +[7,8,9]
print(x)
x.append(0)
print(x)

x,y = [1,2] # Why? No idea, but you should know this exists
