"""2) შექმენით ფუნქცია, რომელიც მიიღებს კვადრატის სიგრძეს თუ სიგრძე არ გადმოგეცემათ ივარაუდოთ რომ ის 10-ია, გამოთვლის მის ფართობსა და პერიმეტრს და დააბრუნებს ერთად. ეს ფუნქცია გამოიძახეთ მინიმუმ 2-ჯერ ერთხელ გადაეცით თქვენთვის სასურველი სიგრძე, მეორედ კი არაფერი გადასცეთ, ორივე შემთხვევაში შეინახეთ ფუნქციის დაბრუნებული მნიშვნელობები ცვლადებში: square_area1, square_perimeter1, square_area2, square_perimeter2"""

def square_properties(length=10):
    area = length ** 2
    perimeter = 4 * length
    return area, perimeter

square_area1, square_perimeter1 = square_properties(5)
square_area2, square_perimeter2 = square_properties()

print(square_area1, square_perimeter1)
print(square_area2, square_perimeter2)