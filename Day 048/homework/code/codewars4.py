"""https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python"""
def reverse_seq(n):
    
    sequence = []
    for i in range (1, n + 1):
        sequence.append(i)
    return sequence[::-1]
    