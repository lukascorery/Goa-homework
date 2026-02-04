# 11) რიცხვების სიაზე "nums = [1, 2, 3, 4, 5, 6]" გამოიყენეთ 'filter' და 'map' ერთად 'lambda'-თან, რათა გაფილტრდეს ლუწები და შემდეგ ყველა ლუწი გაიზარდოს 10-ით
def filter_and_increase_even_numbers(nums):
    filtered = filter(lambda x: x % 2 == 0, nums)
    increased = map(lambda x: x + 10, filtered)
    return list(increased)
