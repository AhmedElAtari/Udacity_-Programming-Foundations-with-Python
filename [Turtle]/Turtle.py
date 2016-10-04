import turtle


window = turtle.Screen() # Create the window
window.bgcolor("#EDEDF1") # Set window color

# declare draw_sqaure function
def draw_rhombus():  
    drawer = turtle.Turtle() # init a turtle named drawer
    drawer.color("#7197AC")   # set color to yellow
    drawer.shape("turtle")   # set shape to turtle
    drawer.speed(15)   # set drawing speed

    # Drawing
    for i in range(0,36):
        drawer.left(110)
        drawer.forward(50)

        drawer.left(70)
        drawer.forward(50)

        drawer.left(110)
        drawer.forward(50)

        drawer.left(70)
        drawer.forward(50)
        
        drawer.right(10)

    drawer.right(90)
    drawer.forward(150)

# Function Call
draw_rhombus()
# click anywhere to close background
window.exitonclick()      

