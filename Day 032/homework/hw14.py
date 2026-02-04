"""14) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else"""

def striconi(text):
    vowels = 'aeiou'
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count