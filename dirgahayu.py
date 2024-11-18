import turtle
import time

screen = turtle.Screen()
screen.title("Dirgahayu Republik Indonesia")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

def write_text_with_shadow(text, x, y, font_size, color, shadow_color, bold=False):
    pen.goto(x + 2, y - 2) 
    pen.color(shadow_color)
    pen.write(text, align="center", font=("Arial", font_size, "bold" if bold else "normal"))
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align="center", font=("Arial", font_size, "bold" if bold else "normal"))

def draw_red_white_flag():
    flag_turtle = turtle.Turtle()
    flag_turtle.speed(2)  
    flag_turtle.penup()
    
    flag_width = 300
    flag_height = 150
    stripe_height = flag_height / 2
    border_color = "gray"
    
    flag_turtle.goto(-flag_width / 2, -flag_height / 2)
    flag_turtle.pendown()
    flag_turtle.pensize(3)
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.forward(flag_width)
        flag_turtle.right(90)
        flag_turtle.forward(stripe_height)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    
    time.sleep(1)
    flag_turtle.penup()
    flag_turtle.goto(-flag_width / 2, -flag_height / 2 + stripe_height)
    flag_turtle.pendown()
    flag_turtle.color("white")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.forward(flag_width)
        flag_turtle.right(90)
        flag_turtle.forward(stripe_height)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    
    time.sleep(1)
    flag_turtle.penup()
    flag_turtle.goto(-flag_width / 2, -flag_height / 2)
    flag_turtle.pendown()
    flag_turtle.color(border_color)
    for _ in range(2):
        flag_turtle.forward(flag_width)
        flag_turtle.right(90)
        flag_turtle.forward(flag_height)
        flag_turtle.right(90)
    
    flag_turtle.hideturtle()

def animate_text():
    text_positions = [
        ("DIRGAHAYU", 0, 130, 36, "black", "gray"),
        ("REPUBLIK INDONESIA", 0, 95, 24, "black", "gray"),
        ("17 AGUSTUS 1945", 0, 65, 24, "black", "gray"),
        ("79", 0, -60, 100, "red", "gray")
    ]
    
    for text, x, y, font_size, color, shadow_color in text_positions:
        write_text_with_shadow(text, x, y, font_size, color, shadow_color)
        time.sleep(1)  

draw_red_white_flag()

animate_text()

turtle.done()
