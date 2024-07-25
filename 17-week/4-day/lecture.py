
# Decorators in Python

# 1. Functions are first-class objects in Python.
# This means they can be passed around and used as arguments.

def greet(name):
    return f"Alright, welcome back in, let's wait until {name} rolls in."



def wrap_greet(funcy_func, name):
    return funcy_func(name)

# print(wrap_greet(greet, "Will"))



# Callbacks

"""
define a function that returns a function.  The returned function should check the name
and print hi if it's will or who are you if it's not
"""


def wrapper_func(func):
    def nested_func(name):
        if name == "will":
            return func(name)
        return "you're not will"
    return nested_func


def say_hello(name):
    # print("hello world")
    return f"hi {name}"

a_nested_func = wrapper_func(say_hello)
print(a_nested_func("bri"))





# 2. Python supports higher-order functions.
# These are functions that take other functions as arguments and/or return functions.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

# Decorating `ordinary` manually without `@`
# pretty = make_pretty(ordinary)
# pretty()
# print()


# 3. Using the @ symbol for decorators.
# The @ symbol offers a shorthand to decorate a function.

@make_pretty
def ordinary():
    print("I am ordinary again")

# ordinary()
# print()











# 4. A more detailed example of a decorator
# This decorator prints statements before and after the decorated function is executed.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# print()


# 5. Decorators that can accept arguments.
# This allows us to decorate functions that accept arguments.

# def my_decorator_with_args(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator_with_args
# def greet_with_name(name):
#     print(f"Hello, {name}!")

# greet_with_name("Alice")
# print()

# @my_decorator_with_args
# def custom_greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# custom_greet("Bob", greeting="Good morning")
