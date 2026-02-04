"""2) შექმენით set სახელად numbers, დაამატეთ მას ორი რიცხვი add() მეთოდით და წაშალეთ ორი ელემენტი remove() მეთოდით. შემდეგ შექმენით მეორე set სახელად even_numbers და გამოიყენეთ union(), intersection(), difference() ორივე set-ზე. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი"""


numbers = set(3, 4 )
numbers.add(1)
numbers.add(2)
numbers.remove(3)
numbers.remove(4)

even_numbers = {0, 2, 4, 6, 8}

union_set = numbers.union(even_numbers)
print(union_set)

intersection_set = numbers.intersection(even_numbers)
print(intersection_set)

difference_set = numbers.difference(even_numbers)
print(difference_set)