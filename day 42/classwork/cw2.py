"""2) კომენტარებით რა არის dictionary, შემდეგ შექმენით 1 dictionary სახელად person რომელშიც გასაღებები იქნება: name, hobby, height, weight. გამოიყენეთ მეთოდები:

clear()
copy()
get()
items()
keys()
values()
pop()
popitem()
update"""


#პითონში dictionary არის მონაცემთა სტრუქტურა, რომელიც ინახავს key-value წყვილებს.


person = {
    "name": "luka", 
    "hobby": "football",
    "height": 162,
    "weight": 53
}

person_copy = person.clear()
person_copy = person.copy()
person_copy = person.get("name")
person_copy = person.items()
person_copy = person.keys()
person_copy = person.values()
person_copy = person.pop("weight")
person_copy = person.popitem()
person.update({"age": 17, "city": "Tbilisi"})