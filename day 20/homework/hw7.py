"""7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)"""

sentence = input("შეიყვანეთ წინადადება: ")
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowel_count = 0
consonant_count = 0

for char in (sentence):
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print(f"ხმოვნების რაოდენობა: {vowel_count}")
print(f"თანხმოვნების რაოდენობა: {consonant_count}")