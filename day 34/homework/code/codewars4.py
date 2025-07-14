"""https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python"""
# Sum of positive
def positive_sum(arr):
    sum = 0
    
    for i in arr:
        if i > 0:
            sum += i
    return sum
        
