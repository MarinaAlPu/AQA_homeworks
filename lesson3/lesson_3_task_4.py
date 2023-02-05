from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(800, 800)

my_turtle.ht()
my_turtle.up()
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.color("blue")

# рисуем круг
def draw_round(t):
    t.down() 
    t.width(2)
    t.forward(10)

# нижний круг
for x in range(0, 60):
    draw_round(my_turtle)
    my_turtle.right(6)

# средний круг
for x in range(0, 45):
    draw_round(my_turtle)
    my_turtle.left(8)

my_turtle.up()
my_turtle.left(90)
my_turtle.forward(255)
my_turtle.right(90)

# голова
for x in range(0, 36):
    draw_round(my_turtle)
    my_turtle.right(10)

my_turtle.up()
my_turtle.right(90)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(90)

# руки
for x in range(0, 12):
    draw_round(my_turtle)
    my_turtle.right(30)

my_turtle.up()
my_turtle.left(180)
my_turtle.forward(170)

for x in range(0, 12):
    draw_round(my_turtle)
    my_turtle.left(30)

my_turtle.up()
my_turtle.backward(85)
my_turtle.right(80)
my_turtle.forward(110)

# глаза
my_turtle.color("black", "black")
my_turtle.begin_fill()
for x in range(4):
    my_turtle.forward(10)
    my_turtle.left(90)
my_turtle.end_fill()

my_turtle.up()
my_turtle.right(100)
my_turtle.forward(40)

my_turtle.color("black", "black")
my_turtle.begin_fill()
for x in range(4):
    my_turtle.forward(10)
    my_turtle.left(90)
my_turtle.end_fill()

my_turtle.up()
my_turtle.home()
#print(my_turtle.position())
my_turtle.right(40)

my_turtle.setposition(49.79,113.22)
my_turtle.right(45)
my_turtle.color("black")
#print(my_turtle.position())

# рот
def draw_round(t):
    t.width(2)
    t.down() 
    t.forward(5)
    t.up() 
    t.forward(5)

for x in range(0, 15):
    draw_round(my_turtle)
    my_turtle.right(12)

# нос
my_turtle.up()
my_turtle.setposition(4.69,92.12)
my_turtle.right(225)
#print(my_turtle.position())

my_turtle.right(30)
my_turtle.down()

my_turtle.color("orange", "orange")
my_turtle.begin_fill()
my_turtle.forward(60)
my_turtle.left(15)
my_turtle.backward(60)
my_turtle.setposition(4.69, 92.12)
my_turtle.end_fill()

# необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()