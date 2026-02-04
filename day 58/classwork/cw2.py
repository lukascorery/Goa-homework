"2) შექმენით Fighter კლასი და გაუწერეთ მინიმუმ 3 ატრიბუტი, შემდეგ შექმნით ამ კლასის 3 ინსტანცია და დაბეჭდეთ ერთ-ერთის თვისებები. დაწერეთ ობიექტზე ორინეტირებული პროგრამირება"
import random

class Troops:
    def __init__(self, name, health, damage, speed, amount, multihit=True, multihit_amount=1):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.amount = amount
        self.multihit = multihit
        self.multihit_amount = multihit_amount

tribesman = Troops("Tribesman", 15, 15, 5, 5)
goblins = Troops("Goblins", 5, 30, 2, 2)
queen = Troops("Queen", 90, 30, 7, 1, True, 3)

