## Getter
class Icon():
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    # getter for ~secret~ password
    @property
    def my_password(self):
        return "somebody's secret password"

my_icon = Icon("blue", "square")
print(my_icon.color)

# call the getter method as if we were just
# reading a property
print(my_icon.my_password)



## Setter
class Icon():
    def __init__(self, color, shape, pswd):
        self.color = color
        self.shape = shape

        # set initial ~secret~ password
        # this calls the setter method!
        self.my_password = pswd

    # getter for ~secret~ password
    @property
    def my_password(self):
        return self._password

    # setter for ~secret~ password
    @my_password.setter
    def my_password(self, new_val):
        print("hashing password....")
        self._password =  str(new_val) + "12345" * 3

my_icon = Icon("blue", "square", "beepboop")
print(my_icon.my_password)

# call the setter method as if we were
# setting my_password as a regular property
my_icon.my_password = "new thing"
print(my_icon.my_password)

