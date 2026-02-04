"""7) შექმენით ლექსიკონი animal, შექმენით მისი ასლი .copy() მეთოდით, შემდეგ კი გამოიყენეთ .clear() ორივეზე (დასაწყისში და ბოლოს დაბეჭდეთ ორივე ლექსიკონი, კომენტარით)"""

animal = {
    "type": "cat",
    "name": "catnip",
    "age": 5
}

animal_copy = animal.copy()


animal.clear()

print("Original:", animal)
print("Copy:", animal_copy)  