"""https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python"""
def find_average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count +=1
        
    if count == 0:
        return 0
    return total/count