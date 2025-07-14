"""4) შექმენით ფუნქცია რომელიც მიიღებს რიცხვს (int) და სიტყვას (string) პარამეტრებად, ფუნქციამ მიღებული სიტყვა უნდა დაბეჭდოს იმდენჯერ რამდენიც არის რიცხვის არგუმენტი"""
def print_word_multiple_times(word, times):
    for _ in range(times):
        print(word)