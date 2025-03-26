"""4) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები"""
temperature = -12
cloudy = True
Winter = True
snow = True
money = False

print(temperature > 30 and not snow ) #false
print(temperature < -12 or money is 12 ) #false
print(snow == False and money is True) #false
print(Winter == False or temperature < -12) #false
print(Winter == False or snow is True) #true