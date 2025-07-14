"""3) მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი"""

number = int(input("Enter a number: "))
total = 0
while number >= 0:
    total += 1
    number = int(input("Enter a number: "))
else:
    print(f"finally, the total is {total}")