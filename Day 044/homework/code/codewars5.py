"""https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python"""

def digitize(n):
    res = []
    
    n = str(n)
    for digit in n:
        res.append(int(digit))
    return res[::-1]
        