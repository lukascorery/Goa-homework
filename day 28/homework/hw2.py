# lower()
"""2) შემოიტანეთ სიტყვა input-ით და დაბეჭდეთ ის პატარა ასოებით"""

word = input("შეიყვანეთ სიტყვა: ")
print(word.lower())

"""3) შემოიტანეთ ორი სიტყვა და შეადარეთ (print(word1 == word2) ისე, რომ არ ჰქონდეს მნიშვნელობა ასოების სიდიდეს (გამოიყენეთ lower)"""
word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")
print(word1.lower() == word2.lower())

"""4) მოცემული სიაა: ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]. ყველა ელემენტი გადააკეთეთ პატარა ასოებად და დაბეჭდეთ (გამოიყენეთ for ციკლი)"""
countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]
for country in countries:
    print(country.lower())