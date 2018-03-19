import turtle

window=turtle.Screen()
window.bgcolor("red")

def draw_square(xd):
    
    for  i in range(1,5):
     xd.forward(100)
     xd.right(90)
    xd.right(15)
    
ash=turtle.Turtle()

ash.color("black")
ash.shape("turtle")

for i in range(1,21):
 draw_square(ash)

# Python27 version
