import turtle as t
import random
screen=t.Screen()
screen.setup(width=500,height=400)
colours=["red","green","yellow","blue","magenta","cyan"]
value=[60,20,-20,-60,-100,-140]
is_race_on=False
all_turtles=[]
for index in range(0,6):
    new_turtle=t.Turtle("turtle")
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.goto(-230,value[index])
    all_turtles.append(new_turtle)
user_bet=screen.textinput(title="MAKE YOUR BET", prompt="WHICH TURTLE WILL WIN THE RACE CHOOSE COLOR ?")
if user_bet:
    is_race_on=True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on=False
            win=t.pencolor()
            if win==user_bet:
                print(f"you win winning turtle is {user_bet} turtle")
            else :
                print(f"you lost winner is {win} turtle")

        speed = random.randint(0, 10)
        t.forward(speed)


screen.exitonclick()