"""https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python"""

def distinct(seq):
    output = []
    for num in seq:
        if num not in output:
            output.append(num)
    return output