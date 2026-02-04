"""https://www.codewars.com/kata/55b42574ff091733d900002f/train/python"""
def friend(x):
    friends = []
    for foe in x:
        if len(foe) ==4:
            friends.append(foe)
    return friends