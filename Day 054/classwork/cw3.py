# 3) შექმენით decorator ფუნქცია, რომელიც თავისთავად შექმნის wrapper ფუნქციას და დააბრუენბს მას. აიღეთ მარტივი greet ფუნქცია რომელიც აბრუნებს "Hello World"-ს და გამოიძახეთ მიანიჭეთ მას decorator. საბოლოოდ გამოიძახეთ greet ფუნქცია


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        result = func()
        print("Something is happening after the function is called.")
        return result
    return wrapper
@my_decorator
def greet():
    return "Hello World" 