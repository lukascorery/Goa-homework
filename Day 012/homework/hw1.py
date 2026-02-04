"""2) გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი"""

#მეტობა >
print(10 > 2)      #True
print(2 > 2)       #False
print(2 > 10)      #False
print(10 > 10)     #False
print(15 > 12)     #True
#მეტობა ან ტოლობა >=
print(20 >= 5)     #True
print(5 >= 20)     #False
print(20 >= 20)    #True
print(5 >= 5)      #True
print(15 >= 12)    #True
#ნაკლებობა <
print(7 < 30)      #True
print(30 < 7)      #False
print(7 < 7)       #False
print(30 < 30)     #False
print(12 < 15)     #True
# ნაკლებობა ან ტოლობა <=
print(9 <= 40)     #True
print(40 <= 9)     #False
print(9 <= 9)      #True
print(40 <= 40)    #True
print(12 <= 15)    #True
#ტოლობა ==
print(50 == 11)    #False
print(11 == 50)    #False
print(50 == 50)    #True
print(11 == 11)    #True
print(12 == 15)    #False
#არ ტოლობა !=
print(100 != 69)   #True
print(69 != 100)   #True
print(100 != 100)  #False
print(69 != 69)    #False
print(12 != 15)    #True
