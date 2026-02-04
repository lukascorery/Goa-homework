# capitalize()
"""8) შემოიტანეთ წინადადება input-ით და გამოიყენეთ capitalize ისე, რომ მხოლოდ პირველი ასო დარჩეს დიდი"""
sentence = input("შეიყვანეთ წინადადება: ")
print(sentence.capitalize())

"""9) მოცემული სტრინგია "gEoRGia". გადააკეთეთ ისე, რომ მხოლოდ პირველი ასო იყოს დიდი, დანარჩენი კი პატარა"""

string = "gEoRGia"
formatted_string = string.capitalize()

"""10) მოცემული სიაა: ["georgia", "aRMENIA", "greeCE"]. ყველა ელემენტს ჯერ გაუკეთეთ lower, შემდეგ capitalize და დაბეჭდეთ"""

countries = ["georgia", "aRMENIA", "greeCE"]
for country in countries:
    print(country.lower().capitalize())

