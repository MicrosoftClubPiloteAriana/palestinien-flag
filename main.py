import turtle

p1 = turtle.Turtle()
p1.penup()
p1.shape('square')
p1.shapesize(stretch_len=900,stretch_wid=8)
p1.color('black')
p1.goto(x=0,y=280)

p2 = turtle.Turtle()
p2.penup()
p2.shape('square')
p2.shapesize(stretch_len=900,stretch_wid=8)
p2.color('green')
p2.goto(x=0,y=-100)

p3 = turtle.Turtle()
p3.penup()
p3.shape('triangle')
p3.shapesize(30)
p3.color('red')
p3.goto(x=-450,y=70)
