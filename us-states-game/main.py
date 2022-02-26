import turtle, pandas
from turtle_pen import TurtlePen

# Initial screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialize turtlePen
turtlePen = TurtlePen()

# Read state information
data = pandas.read_csv("50_states.csv")

# Initialize user guesses and score
allStates = data.state.tolist()
score = 0

# Loop until user guesses all states
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in allStates:
        score += 1
        state_data = data[data.state == answer_state]
        x, y = int(state_data.x), int(state_data.y)
        turtlePen.update(x, y, answer_state)
        allStates.remove(answer_state)
    elif answer_state == "Exit":
        break

    # Handling when a player gets all states right
    if score == 50:
        play = screen.textinput(title=f"{score}/50 States Correct",
                                prompt="You got all states right! \n Good Job!! \n Play again? (y/n))").title()
        if play.lower() == "y":
            score = 0
            allStates = data.state.tolist()
            turtlePen.reset()
        else:
            break

screen.exitonclick()