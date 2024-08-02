# Create a function that returns whether or not the string is a Palindrome.

# Write your function here.
#!!START SILENT
def is_palindrome(string):
  return string == string[::-1]

# Alternate solution using the built-in reversed method
def is_palindrome_reverse(string):
  reverse = ''.join(reversed(string))
  return string == reverse
#!!END


print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False

#!!START SILENT
print(is_palindrome_reverse("kayak")) # True
print(is_palindrome_reverse("app"))  # False
print(is_palindrome_reverse("racecar")) # True
print(is_palindrome_reverse("valid")) # False
#!!END