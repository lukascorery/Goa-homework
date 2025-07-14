"""5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია"""

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
