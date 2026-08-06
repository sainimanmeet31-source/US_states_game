import turtle
import pandas

screen=turtle.Screen()
screen.title('US STATES QUIZ')
image='blank_states_img.gif'
screen.addshape(image)
t=turtle.Turtle()
data=pandas.read_csv('50_states.csv')

turtle.shape(image)
a=0
x=0
y=0

l1=data.state.to_list()


game_is_on=True
while game_is_on:
    answer_state=screen.textinput(title=f'Guess the State{a}/50',prompt='What is another state\'s name?')
    if a==50:
        t.penup()
        t.ht()
        t.goto(-50,0)
        t.write('Game Over',font=('Courier',24,'bold'))
        game_is_on=False
    elif answer_state.lower()=='exit':
        game_is_on=False
    for i in range(len(data['state'])):
        if answer_state.title()==(data['state'][i]):
            l1.remove(answer_state.title())
            a=a+1
            x=int(data['x'][i])
            y=int(data['y'][i])
            t.penup()
            t.ht()
            t.goto(x,y)
            t.write(f'{answer_state.title()}',font=('Courier',10,'normal'))

leftover=pandas.DataFrame(l1)
leftover.to_csv('States_to_learn')
