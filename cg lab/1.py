import turtle
def breshman_line(x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    x_step = 1 if x1 < x2 else -1
    y_step = 1 if y1 < y2 else -1
    line_point = []
    x,y = x1,y1
    line_point.append((x,y))

    if dx>dy:
        error = dx / 2.0
        while x != x2:
            error -= dy
            y += y_step
            error += dx
            x += x_step
            line_point.append((x,y))
    else : 
        error = dy / 2.0
        while x != x2:
            error -= dx
            x += x_step
            eoor += dy
            y += y_step
            line_point.append((x,y))
    return line_point
turtle.setup(500,500)
turtle.speed(0)

x1,y1 = 100,100
x2,y2 = 400,300

line_point = breshman_line(x1,y1,x2,y2)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

for x,y in line_point:
    turtle.goto(x,y)
turtle.exitonclick()