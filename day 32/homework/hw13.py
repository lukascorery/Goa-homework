"""13) დაწერე ფუნქცია, რომელიც იღებს რიცხვს 'n' და აბრუნებს სიას 1-დან 'n'-ის ჩათვლით ყველა ლუწი რიცხვით. გამოიყენე for ციკლი და if-else"""
def get_even_numbers(n):
    even_numbers = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
