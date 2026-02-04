"""https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python"""
def count_sheep(n):
    res = ""
    i = 1
    
    while i <= n:
        res += str(i) + " sheep..."
        i += 1
    return res