"""https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python"""
def find_short(s):
    words = s.split(" ")
    
    shortest = len(words[0])
    
    for word in words:
        length = len(word)
        if length < shortest:
            shortest = length
    return shortest