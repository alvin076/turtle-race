from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []

for _ in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[_])
    turtle.penup()
    turtle.goto(x=-230, y=-100+_*50)
    turtle_list.append(turtle)

end = False

while not end:
    for i in turtle_list:
        i.forward(random.randint(0,10))
        if i.xcor() >= 230:
            winner = turtle_list.index(i)
            end = True

if winner == colors.index(user_input):
    print(f'You\'ve won! The {user_input} turtle is the winner!')
else:
    print(f'You\'ve lost. The {colors[winner]} turtle is the winner!')

screen.exitonclick()
