import turtle
from turtle import *
import random

''' Turtle '''
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
tim.pensize(20)
tim.speed("fastest")
angles = [0, 90, 180, 270]

rgb_colors = [
              (207, 158, 80), (56, 89, 130), (146, 92, 41), (221, 204, 111),
              (139, 26, 46), (134, 175, 201), (157, 46, 87), (44, 55, 105),
              (130, 189, 144), (165, 159, 38), (84, 20, 45), (189, 140, 165),
              (186, 92, 105), (43, 41, 60), (86, 121, 179), (88, 156, 93), (57, 39, 33),
              (80, 153, 165), (194, 83, 73), (46, 74, 77), (79, 74, 45), (161, 202, 220),
              (57, 131, 126), (214, 178, 188), (171, 206, 174), (180, 188, 210)
]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color

def square():
    for i in range(4):
        tim.right(90)
        tim.forward(100)

def dashed_line():
    for i in range(5):
        tim.color(random.choice(rgb_colors))
        tim.forward(0)
        tim.penup()
        tim.forward(50)
        tim.pendown()

def shape_script():
    angle_count = 3
    while angle_count < 10:
        for i in range(angle_count):
            angle = 360 / angle_count
            tim.right(angle)
            tim.forward(100)
        angle_count += 1

def random_walk():
    while True:
        tim.color(random_color())
        #tim.color(random.choice(colors))
        tim.setheading(random.choice(angles))
        tim.forward(30)

def spirograph(tilt_input):
    tilt = 0
    for i in range(100):
        tim.color(random_color())
        tim.setheading(tilt)
        tim.circle(200)
        tilt += tilt_input

def hurst():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    spacing = 50
    rows = 0
    dots_per_row = 10
    for row in range (dots_per_row):
        for col in range(dots_per_row):
            tim.dot(20,random.choice(rgb_colors))
            tim.forward(spacing)
        tim.setheading(90)
        tim.forward(spacing)
        tim.setheading(180)
        tim.forward(spacing * dots_per_row)
        tim.setheading(0)
hurst()
screen = Screen()
screen.exitonclick()