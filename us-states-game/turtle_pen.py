import turtle

# Set text features
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class TurtlePen:
    # Initialize turtlePen
    def __init__(self):
        super(TurtlePen, self).__init__()
        self.turtlePen = turtle.Turtle()
        self.turtlePen.hideturtle()

    # Update a map with answer
    def update(self, x, y, answer_state):
        self.turtlePen.penup()
        self.turtlePen.goto(x, y)
        self.turtlePen.write(answer_state, align=ALIGNMENT, font=FONT)

    # Reset a map when a player want to play again
    def reset(self):
        self.turtlePen.clear()
        self.turtlePen.reset()
        self.turtlePen.hideturtle()
