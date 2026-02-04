"""8) დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და ამატებს ახალ წყვილს ('age': 14) .update() მეთოდით, შემდეგ კი შლის ბოლო ელემენტს .popitem() მეთოდით. დაბეჭდეთ შედეგი და დაუმატეთ კომენტარები"""


def modify_dict(input_dict):

    input_dict.update({'age': 14})

    print("After update:", input_dict)

    input_dict.popitem()

    print("After popitem:", input_dict)
    