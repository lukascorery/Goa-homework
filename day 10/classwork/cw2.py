"""2) მომხმარებელს შემოატანინეთ თავისი სიმაღლე, შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული ინფორმაცია შეინახეთ ცვლადში და გამოუთვალეთ მომხმარებელს სავაურდო სიმაღლე იმ წლების შემდეგ რაც მან შემოიტანა თუ დაუშვათ ყოველ წელს სიმაღლე იზრდება 0.5-ით"""

#შევქმენი სიმაღლის ცვლადი
height = input("what is your hight: ")
#შევცვალე სტრინგიდან ფლოათზე
height = float(height)
#შემოვატანინე მისი ასაკი ინტეგერის სახით
age = int(input("what is your age: "))

#გამოვიტანე მისი საბოლოო სიმაღლე
height = height + (age * 0.5)
#დავპრინტე ეს ყველა
print(height)