"""2) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ."""
cvladi = input("anything u want: ")
print(type(cvladi))

"""3) თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი"""
#str ანუ string ინახავს სტრინგს, ტექსტს. ქვემოთ მოცემული 5 ტიპის სტრინგი
name = "luka"
surname = "shavadze"
type = "books"
knowledge = "100%"
enthusiasm = "0"
#int ანუ integer ინახავს ინტეგერს, მთელ რიცხვს. ქვემოთ მოცემული 5 ტიპის ინტეგერი
age = 17
books = 123
pages = 234
date = 2025
time = 25
#float (ისევ ასე იწერებეა) ანუ არამთელი რიცხვი, წილადი. ქვემოთ მოცემული 5 ტიპის ფლოათი
float = 3.2
height = 200.3
length = 45.1
numbers = 13/3
age1 = 17.3

"""4) აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი."""
str =  "luka"
int = 17
float = 24.4
print(type(str))
print(type(int))
print(type(float))