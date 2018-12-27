#Space war_Developed_JohnMelodyMe
import turtle
import  os

#set_up_the_screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space War")

#Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Player_turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#Main Game Loop
while True:
    #move Enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

#Back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
#player movement
def move_left():
    x = play.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def mov_right():  
    x = player.xcor()
    x -= playerspeed
    if x < 280:
        x =  280
    player.setx(x)

#Keyboard_Binding 
# pip3 install keyboard (Unix)
turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")


delay = raw_input("Press Enter To Finish.")