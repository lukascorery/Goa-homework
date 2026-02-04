"""3) დაწერეთ ფუნქცია, რომელიც იღებს set-ს, ამატებს მას 3 ელემენტს add() მეთოდით, შემდეგ შლის ერთ ელემენტს remove() მეთოდით და აბრუნებს საბოლოო შედეგს"""
def numbers(input_set):
    input_set.add(5)
    input_set.add(6)
    input_set.add(7)
    input_set.remove(5)
    