# # Build a function that can multiply numbers

# # def outter(func):
# #     return func

# # def inner(num):
# #     return num * 2

# # doubler = outter(inner)


# # print(doubler(3))


def outter(num1):
    def inner(num2):
        return num1 * num2

    return inner


# doubler = outter(2)
# tribler = outter(3)


# print(doubler(8))

# print(tribler(10))


## Args n Kwargs
# key word arguments


# def func_with_args(*args, **kwargs):
#     print(args, kwargs)

# func_with_args("will", "zaviar", name3="bri", name4="bobby")


## Sort

some_dict = {"func": lambda x: x + 1}

answer = some_dict["func"]

# print(answer(5))


# print(new_lst)

# lst = [1, 2, 3]

# new_lst = [1 // x for x in lst]

# print(new_lst)
# # lst = [1.0, .5, .33333]

# new_lst = sorted(lst, key=lambda x: 1 / x)

# print(new_lst)


# ## Sorted

# lst = [1, 2, 3]

# new_lst = sorted(lst, key=lambda x: 1 / x)


## Zip
lst = ["will", "bri", "zaviar", "bobby"]
lst2 = ["CST"]

zipped_obj = zip(lst, lst2)

# print("FLAG", list(zipped_obj))


dict1 = {"name": "will"}
dict2 = {"name2": "bri"}

new_dict = {**dict1, **dict2}


# print(new_dict)
## filter

lst = ["will", "bri", "zaviar"]


filter_obj = filter(lambda x: x != "will", lst)

# print(list(filter_obj))

## All and Any

lst = [1, 2, 3]

print(all(lst)) # False
print(any(lst)) # True


num = 1

num2 = 1

def funcy_func():
    x = 1
    return x

return_val = funcy_func()

if(return_val is None):
    print("it was none!")
