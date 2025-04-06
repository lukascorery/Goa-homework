"""2) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ"""
num1 = int(input("number:"))
num2 = int(input("number:"))
num1 -= 1
num2 += 1

for num in range(num1, num2):
    print(num)