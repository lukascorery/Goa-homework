"""1) დასქრინეთ ამოხსნილი codewars-ის ამოცანები და ერთად ჩააგდეთ"""
"""https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python"""
def remove_char(s: str) -> str:
    return s[1:-1]

"""https://www.codewars.com/kata/59a9919107157a45220000e1/train/python"""
def find_all(arr, n):
    result = []
    for i in range(len(arr)):
        if arr[i] == n:
            result.append(i)
    return result
