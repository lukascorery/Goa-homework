"""3) შექმენით პროგრამა რომელიც მოხმარებელს შეეკითხება პაროლს სანამ სწორად არ ჩაწერს"""


password = "luka123"
user_entry = input("password: ")



while user_entry != password:
    user_entry = input("try again: ")