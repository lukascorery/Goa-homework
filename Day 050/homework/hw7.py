# 7) სიტყვების სიაზე "words = ['hello', 'world', 'python']" გამოიყენეთ 'map', რათა ყველა სიტყვა გადაიქცეს დიდ ასოებად


def to_uppercase(words):    
    return list(map(lambda word: word.upper(), words))