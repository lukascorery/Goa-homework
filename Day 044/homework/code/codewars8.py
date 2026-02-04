"""https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python"""
def xo(s):
    s = s.lower()
    count_o = 0
    count_x = 0
    
    for char in s:
        if char == "o":
            count_o += 1
        elif char == "x":
            count_x += 1
            
    return count_o == count_x