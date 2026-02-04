# 1) ახსენით კომნენტარებით raise keyword. მოიყვანეთ raise ბრძანების 2 მაგალითი


index = input("enter a index")
try:
    index = int(index)
except:
    index = input("ennter a number:")


if index < 0:
    raise IndexError("negative index is unacceptable")

if print(index[10]):
    raise TypeError("doesnt exist")


# raise keyword გამოიყენება როდსაცმინდა გამოვიწვიო შეცდომა ალით