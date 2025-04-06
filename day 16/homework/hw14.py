"""შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა"""

code = 2005

entry_pass = " "

trying = 0

while entry_pass != code:
    entry_pass =  int(input("wrong code try again: "))

    trying += 1

print("You are right, it took you " + str(trying) + " tries to get it right  ")
    

    

