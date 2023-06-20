from tkinter import *
from random import randint
from tkinter import ttk
root = Tk()
root.title('rock paper scissors')
root.geometry('480x800')
#change background color to white
root.config(bg='white')

#define images
rock = PhotoImage(file = 'rock.png')
paper = PhotoImage(file = 'paper.png')
scissors = PhotoImage(file = 'scissors.png')
lizard = PhotoImage(file = 'lizard.png')
spock = PhotoImage(file = 'spock.png')

#add images to a list
image_list = [rock, paper,  scissors, lizard, spock]

#pick random number between 0 and 2
pick_number = randint(0,4)

#throw up an image when the program starts
image_label = Label(root, image=image_list[pick_number], bd=0 )
image_label.pack(pady=20)

def spin():
    #pick random number
    pick_number = randint(0,4)
    #show the image
    image_label.config(image=image_list[pick_number])
    if user_choice.get() == 'Rock':
        user_choice_value = 0
    elif user_choice.get() == 'Paper':
        user_choice_value = 1
    elif user_choice.get() == 'Scissors':
        user_choice_value = 2
    elif user_choice.get() == 'Lizard':
        user_choice_value = 3
    elif user_choice.get() == 'Spock':
        user_choice_value = 4


    if user_choice_value == pick_number:
        win_lose_label.config(text='Its a tie')
    elif user_choice_value == 0 and (pick_number == 3 or pick_number==2):
        win_lose_label.config(text='You win!!!')
    elif user_choice_value == 1 and (pick_number == 0 or pick_number==4):
        win_lose_label.config(text='You win!!!')
    elif user_choice_value == 2 and (pick_number == 1 or pick_number==3):
        win_lose_label.config(text='You win!!!')
    elif user_choice_value == 3 and (pick_number == 1 or pick_number==4):
        win_lose_label.config(text='You win!!!')
    elif user_choice_value == 4 and (pick_number == 0 or pick_number==2):
        win_lose_label.config(text='You win!!!')
    else:
        win_lose_label.config(text='Sorry not sorry lol')



#Make our choice
user_choice = ttk.Combobox(root, value=('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'))
user_choice.current(0)
user_choice.pack(pady=20)

#create spin button
spin_button = Button(root, text ='Spin!', command=spin)
spin_button.pack(pady=10)

#Label for showing if you won or not
win_lose_label = Label(root, text ='', font=('Helvetica',18), bg='white', fg='magenta')
win_lose_label.pack()


root.mainloop()


