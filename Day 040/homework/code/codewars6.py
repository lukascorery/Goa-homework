"""https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
"""
def solution(text, ending):
    length_text = len(text)
    lenght_ending = len(ending)
    
    return text[-lenght_ending:] == ending