"""https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python"""
def find_next_square(sq):
    root = 0 
    while (root ** 2) < sq:
        root += 1
    
    if root * root == sq:
        return (root + 1) ** 2
    return -1
