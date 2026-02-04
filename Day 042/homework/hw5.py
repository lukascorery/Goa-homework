"""5) დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და აბრუნებს მის keys-სა და values-ს .keys() და .values() მეთოდებით. დაბეჭდეთ ორივე შედეგი და დაურთეთ კომენტარები"""
def dict_info(input_dict):
    keys = input_dict.keys()
    values = input_dict.values()
    print("Keys:", keys)
    print("Values:", values)
    