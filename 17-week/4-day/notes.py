def name_check(fn):
    def instructor_name(name):
        if name  == "will":
            return "hi Will"
        return fn(name)
    return instructor_name

def what_is_your_name(name):
    return name

res = name_check(what_is_your_name)
print(res("will"))

