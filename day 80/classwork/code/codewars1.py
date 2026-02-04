# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

def most_money(students):
    print(students)
    student_names = []
    student_money = []
    
    
    for student in students:
        student_names.append(student.name)
        student_money.append(student.fives * 5 + student.tens * 10 + student.twenties * 20)
    
    most_money = max(student_money)
    student_index = student_money.index(most_money)
    
    if len(students) > 1 and min(student_money) == max(student_money):
        return "all"
    return student_names[student_index]