"""6) შექმენით ლექსიკონი person და გამოიყენეთ .items() მეთოდი, რათა დაბეჭდოთ ყველა key და value წყვილად. გამოიყენეთ loop და კომენტარი დაუმატეთ შედეგს"""
person = {
    "name": "luka",
    "age": 25,
    "city": "batumi"
}

for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
