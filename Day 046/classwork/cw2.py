"""2) შექმენით რიცხვების სია, შემდეგ ყოველი რიცხვი რომელიც კენტია გაამრავლეთ ორზე და დაამატეთ new_list-ში, ჯერ გააკეთეთ ეს დავალება ჩვეულებრივად, შემდეგ კი list comperhensiosns გამოყენებით. ასევე გააკეთეთ კიდევ 2 მაგალითი თქვენით, პირველ მაგალითში აიღეთ მხოლოდ გამოსახულების დამატება list comperhensions-ში, მეორე მაგალითში კი აიღეთ მხოლოდ პირობა"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for n in numbers:
    if n % 2 != 0:
        new_list.append(n * 2)


new_list_comp = [n * 2 for n in numbers if n % 2 != 0]


example1 = [n * 2 for n in numbers]


example2 = [n for n in numbers if n % 2 != 0]