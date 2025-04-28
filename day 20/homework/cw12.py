"""12) მომხმარებელს შეაყვანინე ინდექსი და ახალი ფერი, შეცვალე ამ ინდექსზე არსებული ფერი სიაში `colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]` და დაბეჭდე განახლებული სია"""

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("შეიყვანეთ ინდექსი: "))
new_color = input("შეიყვანეთ ახალი ფერი: ")

if index == 0: 
    print(colors[0])
    colors[0] = new_color
    print(colors[0])
    
elif index == 1:
    print(colors[1])
    colors[1] = new_color
    print(colors[1])

elif index == 2:
    print(colors[2])
    colors[2] = new_color
    print(colors[2])

elif index == 3:
    print(colors[3])
    colors[3] = new_color
    print(colors[3])



    
