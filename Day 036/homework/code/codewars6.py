"""https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python"""
def capitalize(s, ind):
    result = list(s)
    for index in ind:
        if index < len(result):
            result[index] = result[index].upper()
    return "".join(result)