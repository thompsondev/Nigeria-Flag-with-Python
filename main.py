import turtle
import time

# create a screen
screen = turtle.getscreen()

# set background color of screen
screen.bgcolor("#b3daff")
# set title of screen
screen.title("Nigeria Flag")

# "Yesterday is history, tomorrow is a mystery, 
# but today is a gift. That is why it is called the present.”

oogway = turtle.Turtle()



# set the cursor/turtle speed. Higher value, faster is the turtle
oogway.speed(100)
oogway.penup()
# decide the shape of cursor/turtle
oogway.shape("turtle")

# flag height to width ratio is 2:3
flag_height = 300
flag_width = 450

 
# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -225
start_y = 150

# For saffron, white and green stripes. each strip width will be flag_height/3 = 100
stripe_height = flag_height
stripe_width = flag_width/3

# Radius of Ashok Chakra, half of white stripe 
chakra_radius = stripe_height/3


def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()



# this function is used to create 3 stripes
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 3 stripes,  1 white and 2 green
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#138808")
    # decrease value of y by stripe_height
    x = x + stripe_width
    # create middle white stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    x = x + stripe_width              

    # create last green stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    x = x + stripe_width


def draw_chakra():
    oogway.speed(1)
    oogway.goto(0,0)
    color = "#000080" # navy blue
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(0, 0 - chakra_radius)
    oogway.pendown()
    oogway.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        oogway.penup()
        oogway.goto(0,0)
        oogway.left(15)
        oogway.pendown()
        oogway.forward(chakra_radius)
  
    

# start after 5 seconds.
time.sleep(0)
# draw 3 stripes
draw_stripes()
# draw squares to hold stars




# hide the cursor/turtle
oogway.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()
