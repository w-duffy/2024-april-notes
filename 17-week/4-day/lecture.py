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


def outer_func(func):
    def wrapper(name):
        if name == "will":
            print("in wrapper", func)
            return func(name)
        return "you're not will"

    return wrapper


# def say_hello(name):
#     return f"hi {name}"
# a_nested_func = outer_func(say_hello)
# print(a_nested_func("will"))


@outer_func
def say_hello(name):
    return f"hi {name}"


# print(say_hello("will"))

# @outer_func
# def say_hello_bri(name):
#     return name

# print(say_hello_bri("bri"))


# print(say_hello("will"))

## Let's use our wrapper as a decorator🚀🚀


"""
Pseudo real world exam
"""


def auth_check(route_function):
    def wrapper(req):
        if req["is_logged_in"]:
            route_function(req)
            return
        print("You're being redirected. Please log in")

    return wrapper


@auth_check
def create_spot(req):
    print(f"{req['spot_name']} has been added to the DB")


request = {"spot_name": "Over the water bungalo", "is_logged_in": True}

# create_spot(request)


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


# # 4. A more detailed example of a decorator
# # This decorator prints statements before and after the decorated function is executed.

# # def my_decorator(func):
# #     def wrapper():
# #         print("Something is happening before the function is called.")
# #         func()
# #         print("Something is happening after the function is called.")
# #     return wrapper

# # @my_decorator
# # def say_hello():
# #     print("Hello!")

# # say_hello()
# # print()


# # 5. Decorators that can accept arguments.
# # This allows us to decorate functions that accept arguments.

# # def my_func(name):
# #     print("cool")

# # my_func("will" ,"bri", "sally", "tumr", my_name="will")

# num1 = 1,
# print(num1)

# num1, num2  = 1, 2


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


# @my_decorator_with_args
# def custom_greet(name, greeting="Hello", phrase="niiice"):
#     print(f"{greeting}, {name}! {phrase}")

# custom_greet("Bob", greeting="Good morning")

# dict1  = {"hello": "world"}
# print(dict1["hello"])

# name = "hello"
# print(dict1.name)
# print(dict1["hello"])


# class Dog():
#     def __init__(self, name, my_woof):
#         self.name = name
#         self.my_woof = my_woof
#         self.is_cute = True

#     def __repr__(self):
#         return f"{self.name} said {self.my_woof}"


# fido = Dog("fido")

# # print("down here", fido.name)
# print(fido)


class Dragon:
    def __init__(self, name, color, is_good=True):
        self._name = name
        self._color = color
        self._is_good = is_good

    def breathes_fire(self):
        return f"{self._name} breathes fire everywhere! BURN!!!"

    def change_nature(self):
        self._is_good = not self._is_good
        if self._is_good == True:
            return f"{self._name} is a good dragon!"
        else:
            return f"{self._name} is a bad dragon!"

    def to_dict(self):
        return{
            "name": self._name,
            "color": self._color,
            "is_good": self._is_good
        }

puff = Dragon("puff", "blue")

# print(puff.to_dict())
# print(puff.change_nature())
# print(puff.to_dict())




# SCREAMING_CASE = "don't change this"


class Animal():
    pass

class Cat(Animal):
    pass

class User():
    def __init__(self, name, password, dog="lucky"):
        self._name = name
        self._password = password
        self._dog = dog

    @property
    def my_password(self):
        print("getter called!")
        if True: # hashing algo
            return self._password

    @my_password.setter
    def my_password(self, new_password):
        print("setter called!")
        # hashing and security measures happening here
        self._password = new_password
        return "updated!"

    def to_dict(self):
        return{
            "name": self._name,
            "password": self._password,
            "dog": self._dog
        }

will = User("will", "12345")


print(will.to_dict())
print(will.my_password)
will.my_password = "abcde"
