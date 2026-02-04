"""3) განხილულ მეთოდებზე: split, join, replace, strip მოიყვანეთ 2-2 მაგალითი. თითოეულს მიუწერეთ კომენტარებით ახსნა თუ როგორ მუშაობს"""

text = "hello world python"
print(text.split())

data = "apple,banana,orange"
print(data.split(","))

words = ["hello", "world"]
print(" ".join(words))

letters = ['a', 'b', 'c']
print(" ".join(letters))

text = "I like cats"
print(text.replace("cats", "dogs"))

word = "banana"
print(word.replace("a", "o"))

text = "   hello   "
print(text.strip())

data = ">>>python<<<"
print(data.strip("<>"))
