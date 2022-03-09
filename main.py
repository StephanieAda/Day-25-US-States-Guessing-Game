import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game.')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writing_turtle = turtle.Turtle()

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
all_states_x = data.x.to_list()
all_states_y = data.y.to_list()

game_is_on = True
guessed_states = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?:").title()

while len(guessed_states) < 50:
    print(answer_state)
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        writing_turtle.hideturtle()
        writing_turtle.penup()
        okay = data[data.state == answer_state]
        writing_turtle.goto(int(okay.x), int(okay.y))
        writing_turtle.write(answer_state)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 of the States", prompt="What's another state name?:").title()

for state in guessed_states:
    if state in all_states:
        all_states.remove(i)
missed_states = {
    'You missed these states': all_states
}
print(missed_states)
missed_states_data = pandas.DataFrame(missed_states)
missed_states_data.to_csv("Missed State.csv")
turtle.mainloop()
