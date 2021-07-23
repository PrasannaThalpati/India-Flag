from turtle import *

speed(3)
setup(800,500)

penup()
goto(-400,250)
pendown()

#orange rectangle
color("orange")
begin_fill()
forward(800)
right(90)
forward(180)
right(90)
forward(800)
right(90)
forward(180)
end_fill()

#pen movement
left(180)
penup()
goto(-400,-100)
pendown()


#green rectangle
color("green")
begin_fill()
forward(180)
left(90)
forward(800)
left(90)
forward(180)
left(90)
forward(800)
end_fill()


#ashokchakra
penup()
goto(0,70)
pendown()
color("navy")
begin_fill()
circle(85)
end_fill()

#white circle
penup()
goto(0,60)
pendown()
color("white")
begin_fill()
circle(75)
end_fill()


#bouncing lines
#penup()
#goto(50,-30)
#pendown()
#color("navy")
#left(90)
#for i in range(24):
    #begin_fill()
    #circle(3)
    #end_fill()
    #penup()
    #forward(15)
    #right(15)
    #pendown()

#spokes
color("navy")
begin_fill()
penup()
goto(0,-10)
pendown()
pensize(2)
for i in range(24):
    forward(80)
    backward(80)
    left(15)
hideturtle()

mainloop()

turtle.done()