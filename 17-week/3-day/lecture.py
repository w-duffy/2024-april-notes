"""
Use a set to remove duplicate elements from a list
"""
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
"""
Convert a tuple to a list, and back to a tup
"""



lst = ["hello", "world", "goodbye", "moon"]
"""
Use range with a for loop to print the elements and indices of a list
"""
for i in range(len(num_lst)):
    print(i, num_lst[i])



lst = ["hello", "world", "goodbye", "moon"]
"""
Use enumerate to print the elements and indices of a list
"""



"""
Write a function that takes in a list of numbers and returns
a new list of lists where every element in the new list is 10
greater than the corresponding element in the original list.
"""
nested_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]

def get_new_list(lst):
    pass


print(get_new_list(nested_list))







"""
Write a function that takes in a dictionary and returns
a new dict only if the person lives in EST
"""

dict1 = {"will": "CST", "bri": "EST", "zaviar":"PST", "bobby": "EST"}


def filter_dict(a_dict):
    pass

print(filter_dict(dict1))



"""
Use a dictionary comprehension to create a new dictionary where returns
we only have people that live in EST

"""

dict1 = {"will": "CST", "bri": "EST", "zaviar":"PST", "bobby": "EST"}
