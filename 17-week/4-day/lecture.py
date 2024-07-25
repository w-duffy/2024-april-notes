from datetime import datetime

# our decorator, which takes in a callback function
def timer(func):

    # define the wrapper function that we're going to return
    def wrapper():
        # get current time before function call
        before_time = datetime.now()

        # invoke the callback
        val = func()
        # log the return value of the function
        print(val)

        # get current time after function call
        after_time = datetime.now()

        # calculate total time
        total = after_time - before_time

        # return the total time
        return total

    # decorator returns the wrapper function object
    return wrapper

def my_function():
    return "hello"

my_function = timer(my_function)
print(my_function())
