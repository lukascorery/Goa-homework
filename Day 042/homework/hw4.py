"""4) შექმენით dictionary სახელად student, დაამატეთ მას მონაცემები: name, hobby, height, weight. შემდეგ გამოიყენეთ .get() მეთოდი name-ის მისაღებად და .pop() მეთოდი height-ის წასაშლელად. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი"""

student = {
    "name": "luka",
    "hobby": "Reading",
    "height": 167,
    "weight": 55
}


name = student.get("name")
print(name)

height = student.pop("height")
print(height)