"""https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python"""
def binary_array_to_number(arr):
    binary = ""
    for digit in arr:
        binary += str(digit)
    
    total = 0
    length = len(binary)
    for index in range(length):
        power = length - (index + 1)
        digit = int(binary[index])
        total += (digit * (2 ** power))
    return total