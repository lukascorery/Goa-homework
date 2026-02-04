# 7) დაწერეთ დეკორატორი, რომელიც ფუნქციის გაშვების დროს დაითვლის რამდენი წამი მუშაობდა ფუნქცია


def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"ფუნქცია მუშაობდა {end_time - start_time} წამი")
        return result
    return wrapper

