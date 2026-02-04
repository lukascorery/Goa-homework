"""3) შექმენით ფუნქცია manual_count, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის რაოდენობას სიაში. გამოიყენეთ მხოლოდ loop და if, .count მეთოდის გარეშე"""
def manual_count(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count
