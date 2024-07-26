# Implement a decorator function called chain_decorator that will be used to
# chain function calls. The decorator function should take another function
# argument as a callback, implement two inner wrapper functions, and finally
# return the wrapper function object in each respective wrapper function.

# Implement the inner wrapper function with the following:
# - Takes a variable number of positional and keyword arguments
# - Initializes a variable that calls the callback function with arguments
#   passed to the wrapper
# - Returns the variable multiplied by itself.

# Implement another inner wrapper function with the following:
# - Takes a variable number of positional and keyword arguments
# - Initializes a variable that calls the callback function with arguments
#   passed to the wrapper
# - Returns the variable multiplied by 3

# Finally, be sure to decorate num function using the decorator syntax.

# Write your function here.

def chain_decorator(func):
    print("First")
    def inner(*args):
        res_mult = func(*args)
        return res_mult * res_mult
    return inner

def multiply_by_3(func):
    print("second")
    def wrapper(*args):
        print("mult prints first, but it's not called until it's called in chain")
        res_num = func(*args)
        return res_num * 3
    return wrapper

def num(a, b):
    print("is num first?")
    return a + b

"""----------------------------------------------------"""
# How this is called without Decorators
mult_wrapper = multiply_by_3(num)
chain_wrapper = chain_decorator(mult_wrapper)
print(chain_wrapper(8,2)) # prints 900

"""----------------------------------------------------"""
## With decorators
# @chain_decorator
# @multiply_by_3
# def num(a, b):
#     print("is num first?")
#     return a + b


# print(num(8, 2))  #> 900
# print(num(5, 2))  #> 441
# print(num(4, 9))  #> 1521















### GETTER and SETTER

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


# p = Product(50)
# print(p.price)

# try:
#     p.price = -10
# except ValueError as e:
#     print(e)
