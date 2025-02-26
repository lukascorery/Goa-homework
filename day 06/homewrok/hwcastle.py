"""7) turtle-ში დახაზეთ სასახლე, კოშკზე უნდა იყოს GOA-ს დროშა, ჯგუფიდან საუკეთესო დავალების ავტორი გახდება მინი ლიდერი"""

from turtle import *

#main castle
bgcolor("lightblue")
speed(0)
width(5)
color("black")
penup()
goto(-100, 100)
pendown()
for _ in range(4):
    forward(200)
    right(90)

#leftside of the castle
penup()
goto(-100, 90)
pendown()
right(180)
forward(100)
left(90)
forward(180)
left(90)
forward(100)

#rightside of the castle 
penup()
goto(100, 90)
pendown()
forward(100)
right(90)
forward(180)
right(90)
forward(100)

#furthest left side of the castle
penup()
goto(-200, 200)
pendown()
forward(100)
left(90)
forward(310)
left(90)
forward(100)
left(90)
forward(310)

#furthest right sie of the castle
penup()
goto(200, 200)
pendown()
right(90)
forward(100)
right(90)
forward(310)
right(90)
forward(100)
right(90)
forward(310)

#main caslte add ons (left)
penup()
goto(-70, -100)
pendown()
forward(130)
right(90)
forward(30)
right(90)
forward(130)

penup()
goto(-70, 30)
pendown()
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(50)
right(90)
forward(10)
right(90)
forward(10)

#main castle add ons (right)
penup()
goto(70, -100)
pendown()
right(90)
forward(130)
left(90)
forward(30)
left(90)
forward(130)

penup()
goto(70, 30)
pendown()
left(90)
forward(10)
left(90)
forward(10)
left(90)
forward(50)
left(90)
forward(10)
left(90)
forward(10)

#main castle roof
penup()
goto(-100, 100)
pendown()
right(180)
forward(20)
right(90)
forward(30)
right(90)
forward(240)
right(90)
forward(30)
right(90)
forward(20)

#top of main castle
penup()
goto(-90, 130)
pendown()
right(90)
forward(40)
right(90)
forward(180)
right(90)
forward(40)

penup()
goto(-90, 170)
pendown()
right(90)
forward(10)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(10)

#left castle roof
penup()
goto(-120, 115)
pendown()
for _ in range(4):
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)

#right castle roof 
penup()
goto(120, 115)
pendown()
right(180)
for _ in range(4):
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    

#right middle castle
penup()
goto(200, 160)
pendown()
left(180)
forward(50)
left(90)
forward(50)

#left middle castle
penup()
goto(-200, 160)
pendown()
left(90)
forward(50)
right(90)
forward(50)

#furthest left side of the castle roof
penup()
goto(-300, 200)
pendown()
right(90)
right(60)
forward(30)
right(120)

penup()
goto(-200, 200)
pendown()
left(60)
forward(30)
left(120)
forward(130)

right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(15)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(15)
right(90)
forward(30)
right(90)
forward(30)

#furthest right side of the castle roof
penup()
goto(300, 200)
pendown()
right(180)
right(30)
forward(30)
left(30)

penup()
goto(200, 200)
pendown()
left(30)
forward(30)
right(120)
forward(130)

penup()
goto(185, 230)
pendown()
right(270)

forward(30)
right(90)
forward(30)
right(90)
forward(15)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(10)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(15)
right(90)
forward(30)
right(90)
forward(30)


exitonclick()