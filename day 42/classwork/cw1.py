"""1) შექმენით რიცხვების set, ჩამოწერეთ მისი ყველა თვისება, შემდეგ დაამტეთ და წაშალეთ 2 ელემენტი: add და remove მეთოდების საშვალებით. შემდეგ შექემნით მეორე set და არსებულ 2 set-ს შორის შეასრულეთ სამივე მოქმედება: union, intersection, difference"""

# 1. ar sheicavs duplikatebs
# 2. sheidzleba iyos nebismieri cvladi
# 3. sheidzleba rom ar iyos dalagebuli
num1 = {1, 17, 43, 12, 30, 99, 20}

num1.add(100)  
num1.add(102)

num2 = {12, 30, 99, 100, 101, 20}

num2.remove(101)
num2.remove(99)

print(num1)
print(num2)

nums = num1.union(num2)
print(nums)

nums = num1.intersection(num2)
print(nums)

nums = num1.difference(num2)
print(nums)



