"""https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python"""

def descending_order(num):
    str_num = str(num)
    
    order = sorted(str_num)[::-1]
    joined = "".join(order)
    return int(joined)