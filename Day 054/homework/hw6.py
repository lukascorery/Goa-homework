# 6) დაწერეთ დეკორატორი, რომელიც ფუნქციის გაშვების წინ დაბეჭდავს "ფუნქცია დაიწყო" და დასრულების შემდეგ "ფუნქცია დასრულდა"
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("ფუნქცია დაიწყო")
        result = func(*args, **kwargs)
        print("ფუნქცია დასრულდა")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"გამარჯობა, {name}!")

say_hello("ლუკა")

