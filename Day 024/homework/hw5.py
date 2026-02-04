"""5) შექმენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ string-ს, უნდა იყოს მინიმუმ 20 სიმბოლო, შემდეგ slicing-ის საშვალებით დაბეჭდეთ ეს string ხუთგვარად შემდეგი პირობებით:

მხოლოდ პირველი 5 სიმბოლო,
ბოლო 4 სიმბოლო,
შუა ნაწილი მეოთხე სიმბოლოდან მეათემდე,
მთელი სტრინგი შებრუნებულად,
სტრინგი ამოჭრილი ყოველ მეორე სიმბოლოზე"""

my_string = "my name is luka and i really like doing my homework"


first_five = my_string[:5]
print(first_five)


last_four = my_string[-4:]
print(last_four)


middle_part = my_string[4:10]
print(middle_part)


reversed_string = my_string[::-1]
print(reversed_string)


sliced_string = my_string[::2]
print(sliced_string)