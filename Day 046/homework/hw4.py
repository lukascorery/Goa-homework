"""4) რიცხვების სიიდან "nums = list(range(1, 21))" შექმენით ახალი სია კვადრატებით, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ სცადეთ მსგავსი მაგალითი სხვა მოქმედებით"""

nums = list(range(1, 21))
squared_list = []
for n in nums:
    squared_list.append(n ** 2)

squared_list_comp = [n ** 2 for n in nums]
cubed_list_comp = [n ** 3 for n in nums]
