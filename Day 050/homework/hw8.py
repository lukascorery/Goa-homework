# 8) რიცხვების სიაზე "nums = [5, 8, 11, 14, 17]" გამოიყენეთ 'filter', რათა დატოვოთ მხოლოდ რიცხვები რომლებიც მეტია 10-ზე
def filter_greater_than_ten(nums):
    return list(filter(lambda x: x > 10, nums))