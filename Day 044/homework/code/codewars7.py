"""https://www.codewars.com/kata/56747fd5cb988479af000028/train/python"""
def get_middle(s):
    length = len(s)
    
    if length <= 2:
        return s
    
    if length % 2 == 0:
        start = (length - 2) // 2
        end = start + 2
        return s[start:end]
    else:
        middle_index = length // 2
        return s[middle_index]