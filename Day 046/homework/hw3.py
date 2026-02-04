"""3) სიტყვების სიიდან "words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']" შეარჩიეთ მხოლოდ ისინი, რომლების სიგრძე მეტია 5-ზე, ჯერ "for"-ით, შემდეგ list comprehension-ით"""

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
new_list = []
for word in words:
    if len(word) > 5:
        new_list.append(word)

new_list_comp = [word for word in words if len(word) > 5]