"""https://www.codewars.com/kata/65128732b5aff40032a3d8f0"""
def neutralise(s1, s2):
    result = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            result += "0"
            
    return result