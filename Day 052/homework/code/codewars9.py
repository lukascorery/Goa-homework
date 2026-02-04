# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
    if arr[0] != arr[1]:
        return arr[0] if arr[1] == arr[2] else arr[1]
    common = arr[0]
    for num in arr:
        if num != common:
            return num
