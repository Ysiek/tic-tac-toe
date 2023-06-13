from tkinter import *
import random
from check_file import Check

check_manager = Check()

window = Tk()
window.config(padx=50, pady=50)
window.title("Tic Tac Toe")
buttons = []
player_choices = ['X']
ai_choice = ['0']


def AI_choice(AI_choice_buttons):
    random_button = random.choice(AI_choice_buttons)
    random_button.config(text='0')

    try:
        ai_choice.append(int(str(random_button).replace('.!button', '')) - 1)
    except:
        print("dziala")
        ai_choice.append(0)

    AI_choice_buttons.remove(random_button)
    win = check_manager.check_who_win(ai_choice)
    if win:
        if '0' in check_manager.winner:
            print("przegrales")
        for but in buttons:
            but['state'] = 'disabled'
        return

def player_choice(which_button):
    cur_button = buttons[int(which_button)]
    if cur_button["text"] == 'X' or cur_button["text"] == "0":
        twice()
        return
    cur_button.config(text='X', command=twice)
    player_choices.append(int(which_button))

    win = check_manager.check_who_win(player_choices)
    if win:
        if 'X' in check_manager.winner:
            print("wygrales")
        for but in buttons:
            but['state'] = 'disabled'
        return

    AI_choice_buttons.remove(cur_button)
    if not AI_choice_buttons:
        return print('remis')
    AI_choice(AI_choice_buttons)


def twice():
    print("cannot use this place twice")


# BUTTONS
button = Button(window, width=3, command=lambda m="0": player_choice(m))
button.grid(column=0, row=0, padx=10)
buttons.append(button)

button = Button(width=3, command=lambda m="1": player_choice(m))
button.grid(column=1, row=0)
buttons.append(button)

button = Button(width=3, command=lambda m="2": player_choice(m))
button.grid(column=2, row=0, padx=10)
buttons.append(button)

button = Button(width=3, command=lambda m="3": player_choice(m))
button.grid(column=0, row=1, padx=10, pady=10)
buttons.append(button)

button = Button(width=3, command=lambda m="4": player_choice(m))
button.grid(column=1, row=1, pady=10)
buttons.append(button)

button = Button(width=3, command=lambda m="5": player_choice(m))
button.grid(column=2, row=1, padx=10, pady=10)
buttons.append(button)

button = Button(width=3, command=lambda m="6": player_choice(m))
button.grid(column=0, row=2, padx=10)
buttons.append(button)

button = Button(width=3, command=lambda m="7": player_choice(m))
button.grid(column=1, row=2)
buttons.append(button)

button = Button(width=3, command=lambda m="8": player_choice(m))
button.grid(column=2, row=2, padx=10)
buttons.append(button)

AI_choice_buttons = buttons.copy()

window.mainloop()
