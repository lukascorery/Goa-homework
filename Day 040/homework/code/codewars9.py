"""https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python"""
def is_isogram(string):
    string = string.lower()
    for symbol in string:
        if string.count(symbol) > 1:
            return False
        
    return True