from turtle import Turtle, Screen
import random

# franklin = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Witch turtle will win the race? Enter a colour: ")
print(user_bet)

turtle_names = ["franklin", "funklin", "punklin", "rurklin", "whyklin", "kremuwkin"]
turtle_colours = ["violet", "red", "yellow", "blue", "green", "orange"]
for l in range(len(turtle_names)):
    turtle_names[l]=Turtle()
    turtle_names[l].penup()
    turtle_names[l].shape("turtle")
    turtle_names[l].color(turtle_colours[l])
    turtle_names[l].goto(-230, (-150+(l*50)))






def turtle_moves():
    for s in range(len(turtle_names)):
        speed = random.randint(1, 11)
        distance = random.randint(1, 11)
        turtle_names[s].speed(speed)
        turtle_names[s].forward(distance)


def winner(turtle_number):
    if user_bet == turtle_colours[turtle_number]:
        print(f"The winner is:{turtle_colours[turtle_number]} turtle. You winn")
    else:
        print(f"The winner is:{turtle_colours[turtle_number]} turtle. You loose")


end_of_the_race = False
while not end_of_the_race:
    turtle_moves()
    for n in range(len(turtle_names)):
        x, y = turtle_names[n].position()
        if x >= 220:
            winner(turtle_number=n)
            end_of_the_race = True
            break











screen.exitonclick()