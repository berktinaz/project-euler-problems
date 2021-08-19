from turtle import *

grid_width = 50

TURTLE_SIZE = 20

screen = Screen()

yertle = Turtle(shape="turtle", visible=False)
yertle.penup()
yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
yertle.pendown()
yertle.showturtle()

#screen.mainloop()

def create_grid( size):
    yertle.penup()


    for i in range(1,size+2):
        yertle.dot()
        for j in range(1,size+1):
            yertle.setx(TURTLE_SIZE/2 - screen.window_width()/2 + grid_width * j)
            yertle.dot()
        yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
        yertle.sety( screen.window_height()/2 - TURTLE_SIZE/2 - grid_width * i)

    done()

create_grid(8)
