from tkinter import *
import random

root = Tk()
root.iconbitmap(r'icon.ico')
root.title('Rock Paper Scissors')
root.resizable(width=False, height=False)

click = True

Rock = PhotoImage(file='Rock.png')
Paper = PhotoImage(file='Paper.png')
Scissor = PhotoImage(file='Scissor.png')

Rock_W = PhotoImage(file='Rock_W.png')
Paper_W = PhotoImage(file='Paper_W.png')
Scissor_W = PhotoImage(file='Scissor_W.png')

Rock_L = PhotoImage(file='Rock_L.png')
Paper_L = PhotoImage(file='Paper_L.png')
Scissor_L = PhotoImage(file='Scissor_L.png')

Win = PhotoImage(file='you_win.png')
Lose = PhotoImage(file='you_lose.png')
Tie = PhotoImage(file='Tie.png')

Rock_Button = ''
Paper_Button = ''
Scissor_Button = ''


def game() :
    global Rock_Button, Paper_Button, Scissor_Button

    Rock_Button = Button(root, image=Rock, command=lambda : youPick('Rock'))
    Paper_Button = Button(root, image=Paper, command=lambda : youPick('Paper'))
    Scissor_Button = Button(root, image=Scissor, command=lambda : youPick('Scissor'))

    Rock_Button.grid(row=0, column=0)
    Paper_Button.grid(row=0, column=1)
    Scissor_Button.grid(row=0, column=2)


def bot() :
    bothand = random.choice(['Rock', 'Paper', 'Scissor'])
    return bothand


def youPick(playerhand):
    global click
    bothand = bot()

    if click == True:
        if playerhand == 'Rock':
            if bothand == 'Rock':
                Rock_Button.configure(image=Rock_L)
                Paper_Button.configure(image=Rock_L)
                Scissor_Button.configure(image=Tie)
                click = False
            elif bothand == 'Paper':
                Rock_Button.configure(image=Rock_L)
                Paper_Button.configure(image=Paper_W)
                Scissor_Button.configure(image=Lose)
                click = False
            else:
                Rock_Button.configure(image=Rock_W)
                Paper_Button.configure(image=Win)
                Scissor_Button.configure(image=Scissor_L)
                click = False

        if playerhand == 'Paper':
            if bothand == 'Paper':
                Rock_Button.configure(image=Paper_L)
                Paper_Button.configure(image=Paper_L)
                Scissor_Button.configure(image=Tie)
                click = False
            elif bothand == 'Scissor':
                Rock_Button.configure(image=Scissor_W)
                Paper_Button.configure(image=Paper_L)
                Scissor_Button.configure(image=Lose)
                click = False
            else:
                Rock_Button.configure(image=Rock_L)
                Paper_Button.configure(image=Paper_W)
                Scissor_Button.configure(image=Win)
                click = False

        if playerhand == 'Scissor':
            if bothand == 'Scissor':
                Rock_Button.configure(image=Tie)
                Paper_Button.configure(image=Scissor_L)
                Scissor_Button.configure(image=Scissor_L)
                click = False
            elif bothand == 'Rock':
                Rock_Button.configure(image=Rock_W)
                Paper_Button.configure(image=Lose)
                Scissor_Button.configure(image=Scissor_L)
                click = False
            else:
                Rock_Button.configure(image=Rock_L)
                Paper_Button.configure(image=Win)
                Scissor_Button.configure(image=Scissor_W)
                click = False
    else:
        if playerhand == 'Rock' or playerhand == 'Paper' or playerhand == 'Scissor':
            Rock_Button.configure(image=Rock)
            Paper_Button.configure(image=Paper)
            Scissor_Button.configure(image=Scissor)
            click = True


game()

root.mainloop()
