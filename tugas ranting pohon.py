#KELOMPOK 6
#1.LALU GUNAWAN JAYADI EFENDI
#2.LALU ARIF RAHMAN HAKIM
#3.MUHAMAD AMIZA SURYA
#4.IRA RASILA WATIN
#5.NENTI AULIA NATASYA
import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def draw_tree():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.pensize(2)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)

    draw_branch(100, t)

    t.hideturtle()
    screen.mainloop()

draw_tree()
