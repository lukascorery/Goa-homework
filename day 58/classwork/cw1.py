"""1) დაწერეთ რა არის scope თქვენი სიტყვებით და მოიყვანეთ 3 მაგალითი"""
# scoping - არის რაიმე ფუნქციის ხილვადობა, თუ რა მანძილზე აქვს მას წვდომა მთავარ კოდში

def outer_scope():
    name = "luka"
    def inner_scope():
        age = 14
        print(name, age)
    inner_scope()