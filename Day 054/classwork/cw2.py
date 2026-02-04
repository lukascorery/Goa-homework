# 2) შექმენით ფუნქცია greet_people რომელსაც ექენბა 3 არგუემნტის ცვლადი, special, *guests, **visitors. თქვენი ფანტაზიით მიესალმეთ თითეულს განსხვავებულად. ახსენით რა არის *args და **kwargs


def greet_people(special, *guests, **visitors):
    print(f"Hello {special}, you are our special guest today!")

    for guest in guests:
        print(f"Welcome {guest}, we are glad to have you here.")

    for title, name in visitors.items():
        print(f"Greetings {title} {name}, thank you for visiting us.")
        

    