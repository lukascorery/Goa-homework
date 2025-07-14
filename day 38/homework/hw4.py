"""4) შექმენით სიები fruits, colors, numbers. თითოეულზე გამოიყენეთ index, count, sort, sorted, min, max მეთოდები & ფუნქციები და დააკომენტარეთ თითოეული მაგალითი (რას აკეთებს)"""
fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi']
colors = ['red', 'blue', 'green', 'blue', 'yellow']
numbers = [42, 17, 23, 17, 99, 5]

# აბრუნებს პირველი შემხვედრი ელემენტის ინდექსს სიაში
print(fruits.index('apple'))  
print(colors.index('blue'))    
print(numbers.index(17))       


# ითვლის რამდენჯერ გვხვდება კონკრეტული ელემენტი სიაში
print(fruits.count('apple'))   
print(colors.count('blue'))    

# ალაგებს სიას ადგილზე (შეცვლის სიას თვითონ)
fruits.sort()
print(fruits)             
colors.sort()
print(colors)         
numbers.sort()
print(numbers)              


# აბრუნებს სორტირებულ სიას მაგრამ არ ცვლის ორიგინალს
print(sorted(fruits))          
print(sorted(colors))          
print(sorted(numbers, reverse=True))  


# აბრუნებს მინიმალურ მნიშვნელობას სიაში
print(min(fruits))             
print(min(colors))             
print(min(numbers))            


# აბრუნებს მაქსიმალურ მნიშვნელობას სიაში
print(max(fruits))             
print(max(colors))             
print(max(numbers))            