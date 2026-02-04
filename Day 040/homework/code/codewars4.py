"""https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python"""

def reverse_words(s):
    words = s.split()
    words = words[::-1]
    return " ".join(words)