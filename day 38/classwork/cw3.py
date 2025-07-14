"""3) შექმენით list, tuple და set. კომენტარებით დაწერეთ თითოეულის თვისება და ყველა თვისებიდან მოიყვანეთ მაგალითები"""

list_example = ["apple", "banana", "cherry"]
tuple_example = ("dog", "cat", "mouse")
set_example = {"red", "green", "blue"}

# List: დალაგებული, შეცვლადი, დუპლიკატების დაშვება
list_example.append("orange") 

# Tuple: დალაგებული, შეუცვლელი, დუპლიკატების დაშვება
tuple_example = tuple_example + ("fish",)


# Set: არალინარიული, შეცვლადი, არ უშვებს დუპლიკატებს
set_example.add("yellow")


