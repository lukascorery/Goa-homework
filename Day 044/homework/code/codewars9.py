"""https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python"""
def to_jaden_case(string):
    words = string.split(" ")
    res = []
    
    for word in words:
        res.append(word.capitalize())
    return " ".join(res)