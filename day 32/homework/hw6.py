"""6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს"""

def calculate_average(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)

