# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            position = ord(lower_char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)
