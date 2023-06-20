
from tkinter import *
from random import randint
from tkinter import ttk
root = Tk()
root.title('rock paper scissors')
root.geometry('500x600')
#change background color to white
root.config(bg='white')

#define images
rock = PhotoImage(file = 'rock.png')
paper = PhotoImage(file = 'paper.png')
scissors = PhotoImage(file = 'scissors.png')

#add images to a list
image_list = [rock, paper,  scissors]

#pick random number between 0 and 2
pick_number = randint(0,2)

#throw up an image when the program starts
image_label = Label(root, image=image_list[pick_number], bd=0 )
image_label.pack(pady=20)

#create spin function
def spin():
    #pick random number
    pick_number = randint(0,2)
    #show the image
    image_label.config(image=image_list[pick_number])

    #0 = rock
    #1 = paper
    #2  = scissors
    #convert dropdown choice to a number
    if user_choice.get() == 'Rock':
        user_choice_value = 0
    elif user_choice.get() == 'Paper':
        user_choice_value = 1
    elif user_choice.get() == 'Scissors':
        user_choice_value = 2

    #determine if you won or lost
    if user_choice_value == 0:
        if pick_number == 0:
            win_lose_label.config(text ='Its a tie')
        elif pick_number == 1:
            win_lose_label.config(text='Paper covers rock, you lose!')
        elif pick_number == 2:
            win_lose_label.config(text='Rocks smashes scissors, you win!')


    if user_choice_value == 1:
        if pick_number == 0:
            win_lose_label.config(text ='Paper covers rock, you win')
        elif pick_number == 1:
            win_lose_label.config(text='its a tie!')
        elif pick_number == 2:
            win_lose_label.config(text='scissors cut paper you lose!')


    if user_choice_value == 2:
        if pick_number == 0:
            win_lose_label.config(text ='Rock smashes scissors, you lose!')
        elif pick_number == 1:
            win_lose_label.config(text='scissors cut paper you win')
        elif pick_number == 2:
            win_lose_label.config(text='Its a tie!')

#Make our choice
user_choice = ttk.Combobox(root, value=('Rock', 'Paper', 'Scissors'))
user_choice.current(0)
user_choice.pack(pady=20)

#create spin button
spin_button = Button(root, text ='Spin!', command=spin)
spin_button.pack(pady=10)

#Label for showing if you won or not
win_lose_label = Label(root, text ='', font=('Helvetica',18), bg='white')
win_lose_label.pack(pady=30)


root.mainloop()
