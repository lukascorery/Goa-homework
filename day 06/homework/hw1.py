"""3) შექმენით ცვლადი სახელად celsius სადაც შეინახავთ მთელ რიცხვს. შემდეგ შექმენით ცვლადი სახელად fahrenheit, სადაც უნდა გამოთვალოთ წინა ცვლადის ტემპერატურა რამდენი ფაერენგეიტი იქნება. ასევე შექმენით ცვლადი kelvin რომელშიც შეინახავთ თუ რამდენი კელვინი იქნება celsius ცვლადში მოცემული რიცხვი, საბოლოოდ დაბეჭდეთ სამივე ცვლადი"""

celsius = input("what is celsius right now? ")
fahrenheit = int(celsius) * 9/5 + 32
kelvin = int(celsius) + 273.15

print(celsius)
print(fahrenheit)
print(kelvin)