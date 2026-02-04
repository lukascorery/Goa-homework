"""1) შექმენით student dictionary, რომელშიც გექნებათ მინიმუმ 4 ელემენტი. შემდეგ გამოიყენეთ მეთოდები ამ dictionary-ზე

.update()
.pop()
ელემენტი შეცვალეთ"""


student = {
    "name": "Luka",
    "age": 17,
    "city": "Batumi",
    "major": "Computer Science"
}


student.update({"age": 26})


student.pop("city")


student["major"] = "Software Engineering"
