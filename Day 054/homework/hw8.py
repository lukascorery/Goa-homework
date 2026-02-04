# 8) შექმენით ფუნქცია 'multiply', რომელიც იღებს რიცხვებს 'args'-ით და აბრუნებს მათ ნამრაველს

num = (1, 2, 3, 4, 4, 4, 5, 5)

def multiplier(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiplier(*num))