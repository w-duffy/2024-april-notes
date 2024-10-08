# Majority Character

# Given a string, write a function named majority_char that returns the
# character that is the majority of the string. If there is no majority
# character, return None. A majority is considered as having more than n / 2
# instances where n is the length of the string.


#!!START
def majority_char(str):
    counter = {}
    for char in str:
        if counter.get(char):
            counter[char] += 1
        else:
            counter[char] = 1
        if counter[char] > len(str) / 2:
            return char
    return None
#!!END

str = 'all'
str2 = 'welcome to the jungle'

print(majority_char(str))           # 'l'
print(majority_char(str2))          # None
