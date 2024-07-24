# num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# """
# Use a set to remove duplicate elements from a list
# """
# # print(list(set(num_lst)))


# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# """
# Convert a tuple to a list, and back to a tup
# """
# # lst = list(tup)
# # print(lst)
# # back_to_tup = tuple(lst)
# # print(back_to_tup)


# lst = ["hello", "world", "goodbye", "moon"]
# """
# Use range with a for loop to print the elements and indices of a list
# """

# # for i in range(len(lst)):
# # print(i, lst[i])


# lst = ["hello", "world", "goodbye", "moon"]
# """
# Use enumerate to print the elements and indices of a list
# """
# # print(list(enumerate(lst)))
# # for i, el in tuple(enumerate(lst)):
# #     print(i, el)

# # comp = list(enumerate(lst))
# # print(comp)


# """
# Write a function that takes in a list of lists where elements are numbers and returns
# a new list of lists where every element in the new list is 10
# greater than the corresponding element in the original list.
# """
two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]

def get_new_list(outer_list):
    new_list = []
    for lst in outer_list:
        new_nested_lst = []
        for ele in lst:
            new_nested_lst.append(ele + 10)
        new_list.append(lst)
    return new_list

print(get_new_list(two_dimensional_list))  # [[11, 12], [14, 15, 16], [17, 18, 19, 20]]


"""
Use a list comprehension
"""
two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]
# # Try breaking it down into smaller peices to test pieces individually first
# lst = [1, 2] # just using a smaller piece of data to make sure the comprehension works
# new_lst = [el + 10 for el in lst] # prints [10, 12] -- Perfect!


def get_new_list(lst):
    # [print(el) for el in lst] # prints [1, 2], [4, 5, 6], [7, 8, 9, 10]
    # return [print(el) for el in lst]  # we're going to replace print(el) with the comprehension above on line 62
    return [[num + 10 for num in el] for el in lst]


print(get_new_list(two_dimensional_list))  # [[11, 12], [14, 15, 16], [17, 18, 19, 20]]


"""
Use map with a list comprehension
"""
# # Try completing the pieces individually first
# lst = [1, 2] # just using a smaller piece of data to make sure map and lambda work
# anon_func = lambda x: x + 10
# anon_func(2) # Prints 12
# new_list = list(map(lambda x: x + 10, lst))
# print("Just testing the map", new_list) # prints [10, 12]

two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]

def get_new_list(lst):
    # We know the map and lambda work, so let's replace the nested comprehension with our map
    # return [[num + 10 for num in el] for el in lst] # Replace this: [num + 10 for num in el] with the map on line 80
    return [list(map(lambda x: x + 10, el)) for el in lst]


print(get_new_list(two_dimensional_list))  # [[11, 12], [14, 15, 16], [17, 18, 19, 20]]


# """
# Write a function that takes in a dictionary and returns
# a new dict only if the person lives in EST
# """

dict1 = {"will": "CST", "bri": "EST", "zaviar": "PST", "bobby": "EST"}

def filter_dict(a_dict):
    new_dict = {}
    for key, val in a_dict.items():
        if val == "EST":
            new_dict[key] = val
    return new_dict

print(filter_dict(dict1))


"""
 Use a dictionary comprehension to create a new dictionary where returns
we only have people that live in EST
"""

dict1 = {"will": "CST", "bri": "EST", "zaviar": "PST", "bobby": "EST"}

def filter_dict(a_dict: dict):
    new_dict = {key: val for key, val in a_dict.items() if val == "EST"}
    return new_dict

print(filter_dict(dict1))
