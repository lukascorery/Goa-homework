"""5) დაწერეთ ფუნქცია, რომელიც მიიღებს სიას და დაბეჭდავს უნიკალურ ელემენტებს და მათ რაოდენობას სიაში, მაგ: apple - 2, banana - 3... გამოიყენეთ .count მეთოდი"""
def elements(input_list):

    elements = set(input_list)
    for element in elements:
        count = input_list.count(element)  
        print(f"{element} - {count}")
