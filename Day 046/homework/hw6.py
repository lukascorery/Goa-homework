"""6) სიიდან "animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']" შექმენით ახალი სია, რომელიც შეიცავს სიტყვების პირველ ასოებს, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ აირჩიეთ მხოლოდ ის სიტყვები, რომლებიც "e"-ზე იწყება"""


animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = []
for animal in animals:
    first_letters.append(animal[0])
first_letters_comp = [animal[0] for animal in animals]
e_animals = [animal for animal in animals if animal[0] == 'e']


