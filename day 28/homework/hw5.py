# find()
"""11) შემოიტანეთ სიტყვა input-ით და მოძებნეთ ასო a-ს პირველი პოზიცია"""

word = input("შეიყვანეთ სიტყვა: ")
position = word.find('a')
print( position)

"""12) მოცემული სტრინგია "I visited Georgia, Armenia and Greece". მოძებნეთ Armenia და დაბეჭდეთ მისი პოზიცია"""

text = "I visited Georgia, Armenia and Greece"
position = text.find("Armenia")
print(position)

"""13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found"""

search_word = input("შეიყვანეთ საძიებელი სიტყვა: ")
search_position = text.find(search_word)
if search_position != -1:
    print(search_position)
else:
    print("word not found") 
