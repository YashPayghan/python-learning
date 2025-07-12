import random
import turtle as t
from turtle import Screen
colors_list=[(233, 233, 232), (237, 232, 234), (231, 233, 238), (224, 233, 227), (207, 160, 81), (56, 88, 130), (144, 91, 41), (139, 27, 48), (221, 207, 108), (134, 177, 201), (157, 47, 85), (43, 54, 105), (170, 159, 41), (130, 189, 144), (83, 20, 43), (39, 43, 64), (185, 95, 108), (189, 140, 166), (86, 122, 180), (59, 40, 31), (89, 157, 93), (80, 153, 165), (194, 80, 73), (45, 75, 77), (160, 201, 219), (54, 129, 127), (80, 75, 44), (218, 176, 186), (46, 74, 73), (170, 206, 167), (221, 180, 168), (179, 188, 211), (143, 37, 35), (43, 63, 62)]
t.colormode(255)
t = t.Turtle()
screen = Screen()
for y in range (-200,0,20):
    t.penup()
    t.goto(-200, y)
    t.pendown()
    for value in range(-200,0,20):
        t.dot(10, random.choice(colors_list))
        t.penup()
        t.goto(value,y)
        t.pendown()
        t.dot(10, random.choice(colors_list))

screen.exitonclick()