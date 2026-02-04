# 10) დაწერეთ დეკორატორი, რომელიც ფუნქციის დაბრუნებულ ტექსტს გადააქცევს დიდ ასოებად

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        print("შესავალი")
        result = func(*args, **kwargs)      
        result = result.upper()             
        print("დასასრული")
        return result
    return wrapper


