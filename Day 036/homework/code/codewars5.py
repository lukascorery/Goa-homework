"""https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python"""
def is_digit(n):
    if len(n) == 1:
        for i in n:
            if i.isdigit():
                return True
    return False

