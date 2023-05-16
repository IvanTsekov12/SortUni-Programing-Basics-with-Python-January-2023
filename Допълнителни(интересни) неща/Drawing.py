import turtle

t = turtle.Pen()
turtle.bgcolor('black')

color_count = 6

for x in range(360):
    if x % color_count == 0:
        t.pencolor("red")
    elif x % color_count == 1:
        t.pencolor("purple")
    elif x % color_count == 2:
        t.pencolor("blue")
    elif x % color_count == 3:
        t.pencolor("green")
    elif x % color_count == 4:
        t.pencolor("orange")
    elif x % color_count == 5:
        t.pencolor("yellow")
    t.width(x // 100 + 1) # Прави размера на химикала по-дебел
    t.forward(x)
    t.left(59)
