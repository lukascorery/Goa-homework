"""2) მოხმარებელს შემოატანინეთ თავისი გამოცდის ქულა, შემდეგ პირობითი განხცადების საშვალებით შეამოწმეთ ეს ქულა მეტია თუ 50-ზე, თუ მეტია დაუბეჭდეთ რომ გამოცდა ჩააბარა"""


point = int(input("what did you get: "))
if point > 50:
    print("you passed")
else:
    print("too bad.")


" bonu "
if point %2 == 0:
    print("even")
else:
    print("odd")