## Falseys 0, 0.0, "", [], set(), {}, range(), False, None

# var = []
# if []:
#     print("hi")


# Python Scoping

# def make_a_five():
#     y = 5
#     return y

# ## this is in the global scope
# if True:
#     x = 10


# # print(x) #10
# # `x` was created in the global scope

# print(y) # NameError: name 'y' is not defined
# # # `y` was created in the scope of the make_a_five function

float(1)
int(1.0)

# print("first", lst)

# SCREAMING_CASE = [["dog", "cat"], ["yellow", "bat"]]

# Single index: list_name[single_index]
# # Index range: list_name[start:stop:step]
# my_string = "hello"
# # print(my_string[2])

# print(lst[-1])
# lst = [1, 2, 3, 4, 5, 6]

# new_lst = lst[::]

# print("lst", lst)

# print("new lst", new_lst)

# print(lst == new_lst)

# print(lst is new_lst)

# # print("seco lst)

# # print(lst)

# x = 1
# b = 1
# c = 1


# # ab = "hello"

# # de = "hello"
# # print(id(ab), id(de))


# print(id("a"), id("A"))
# TODO
# # print("string ids:", id(str(x)), id(str(y)))  # different places in memory
# # print("integer ids:", id(x), id(int(y)))  # same place in memory


# new_str = "abc"
# new_str_2 = "2"
# print(int(new_str))
# print(int(new_str_2))
# # lst = [1,2,3]


# functions
# lst = "hello world 123"
# copy_lst = lst[::]
# print(lst, copy_lst)

# print(lst == copy_lst)
# print(lst is copy_lst)


def last_three(string, last):
    if string.lower()[-3:] is last.lower():
        print(string.lower()[-3:])
        print(last.lower())
        return True
    else:
        return False


# print(last_three("Power", "wer"))  #> True
# print("Power".lower()[-3:])
# new_str = "Power".lower()[-3:]
# newer_str = "wer".lower()
# print(id(new_str))
# print(id(newer_str))


# if "yes":
#     print("world")

the_name = "Bri"

# def say_hi(name):
#     if name == "Will" or name == "Bri":
#         print("coming from the func", "Will")
#         return "nice"

# returns_anything = say_hi(the_name)
# print("Returned value", returns_anything)

# print(say_hi(the_name))
lst_of_names = ["will", "bri"]

# Write a function that takes in a list of names and returns
# a new list with y at the end


# concat_str = "string 1 " "string 2"


# print(concat_str)
# def y_names(lst):
#     new_lst = []
#     index = 0
#     while index < len(lst):
#         new_lst.append(lst[index] + "y")
#         index += 1
#     return new_lst


# print(y_names(lst_of_names))


# # Lambda Functions

# map_obj = map(lambda x: x + 2, [1,2,3])

# return_val = anon_func(3) # print 5
# print("In Python World", return_val)


# [1,2].append(5)


# def string_multi_print(str):
#     return lambda num: print(str * num)

# inner_func = string_multi_print("hello ")
# inner_func(5)

# string_multi_print("hello ")(2)  # Prints "hello hello "
# string_multi_print("wahoo ")(3)  # Prints "wahoo wahoo wahoo "


# anon_func = lambda x: x + 2


# print(anon_func(3))

# lst = [1,2,3]

# new_lst = list(map(lambda x: x + 2, lst))


for el in lst:
    new_lst.append(el + 10)

# print("completed new list!", new_lst)


# Non List Comp
lst = [1, 2, 3]
new_lst = []
for el in lst:
    lst.append(el + 10)
    

# List Comp
lst = [1, 2, 3]

new_list = [el + 10 for el in lst]

print(new_list)
