# 5) შექმენით 'lambda' ფუნქცია, რომელიც გადაყავს ცელსიუსი ფარენჰეიტში და გამოიყენეთ 'for' ციკლში

def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    for c in celsius_list:
        fahrenheit = (c * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list