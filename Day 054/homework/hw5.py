# 5) შექმენით ფუნქცია, რომელიც მიიღებს 'kwargs'-ით მანქანის მონაცემებს და დაბეჭდავს თითოეულ გასაღებს და მნიშვნელობას

car = {
    "model": "mazda",
    "age" : 2025
}

def cars (**kwargs):
    for key, value in kwargs.items():
        print(f"მოდელი: {key}, ასაკი: {value}")

cars(**car)