# 9) შექმენით ფუნქცია, რომელიც იღებს 'args'-ით რიცხვებს და აბრუნებს მათ მაქსიმუმს და მინიმუმს
def numbers(*args):
    maximum = max(args)
    minimum = min(args)
    return minimum, maximum

num = (1,2,3,4,3,4,4,4,3)

print(numbers(*num))
