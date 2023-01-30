# Like a list, but immutable
# You can't change it
# So, everything you do with a list, that doesn't modify it
# you can do with a tuple, next

my_list = [1,2,3]
my_tuple = (1,2,3)

x,y,z = (1,2,3) # Now, it does make sense, since tuples are not dynamic

# You can use tuples for multiple returns
def sum_and_product(x,y):
    return (x+y),(x*y)

new_tuple = sum_and_product(2,5)
var_sum,var_product = sum_and_product(2,5)
print(new_tuple)
print(var_sum)
print(var_product)