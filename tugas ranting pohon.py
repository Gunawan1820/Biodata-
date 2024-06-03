import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        # Draw the branch
        t.forward(branch_length)
        # Draw right subtree
        t.right(20)
        draw_branch(branch_length - 15, t)
        # Draw left subtree
        t.left(40)
        draw_branch(branch_length - 15, t)
        # Return to original orientation
        t.right(20)
        t.backward(branch_length)

def draw_tree():
    # Set up the turtle
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

    # Draw the tree
    draw_branch(100, t)

    # Finish up
    t.hideturtle()
    screen.mainloop()

# Run the function
draw_tree()
