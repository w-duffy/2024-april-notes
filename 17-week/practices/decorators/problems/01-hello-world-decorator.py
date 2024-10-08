# Implement a decorator function called `hello_world_decorator` that will be
# used to `print` statements. The decorator function should take another
# function argument as a callback, implement an inner wrapper function, and
# finally return the wrapper function object.

# Implement the inner wrapper function with the following:
# - A print statement of the string "Hello"
# - Calls the callback function
# - Another print statement after the callback containing the string "Goodnight"
 
# Finally, be sure to decorate the `world` function using the decorator syntax.

# Write your function here.
#!!START SILENT
def hello_world_decorator(func):
  def inner():
    print("Hello")
    func()
    print("Goodnight")
  return inner

@hello_world_decorator
#!!END
def world():
  print("World")

world() #> Hello World Goodnight