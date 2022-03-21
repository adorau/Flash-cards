from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
POLISH = "Polish"
SPANISH = "Spanish"
spanish_words = []
learned_words = []

#------------------- POLISH WORDS ------------------------#

def polish_word():
    new_canvas = canvas.itemconfig(image_canvas, image=front_image_polish)
    canvas_title_polish = canvas.itemconfig(canvas_title, text=POLISH)
    canvas_item_polish = canvas.itemconfig(canvas_item, text=current_card["Polish"])

#-------------------CHOOSING WORDS SPANISH------------------------#

def remove_save(remove=True):
    df = pandas.read_csv('słowka.csv', sep=';')
    global dict_from_csv
    dict_from_csv = df.to_dict(orient="records")
    if remove:
        dict_from_csv.remove(current_card)
        learned = pandas.DataFrame(dict_from_csv)
        learned.to_csv('słowka.csv', index=False, sep=';')


def add_save():
    try:
        df = pandas.read_csv('list_of_learned_words.csv', sep=';')
        learned_csv = df.to_dict(orient="records")
    except:
        learned_csv = []
    learned_csv.append(current_card)
    learned = pandas.DataFrame(learned_csv)
    learned.to_csv('list_of_learned_words.csv', index=False, sep=';')


#-------------------NEXT CARD/SAVING------------------------#

def no_button():
    next_card(no_button=True)


def yes_button():
    next_card(no_button=False)


def next_card(no_button=True):
    global current_card, timer
    current_card = random.choice(dict_from_csv)
    window.after_cancel(timer)
    canvas.itemconfig(image_canvas, image=front_image_spanish)
    canvas.itemconfig(canvas_title, text=SPANISH)
    canvas.itemconfig(canvas_item, text=current_card["Spanish"])
    canvas.update()
    timer = window.after(3000, polish_word)

    if no_button == False:
        add_save()
        remove_save()

#-------------------TK WINDOW------------------------#

window = Tk()
window.config(background=BACKGROUND_COLOR, padx=20, pady=20)

timer = window.after(3000, polish_word)
remove_save(remove=False)

#-------------------BUTTONS------------------------#

no_image = PhotoImage(file=".\images\wrong.png")
no_button = Button(image=no_image, highlightthickness=0, bd=0, anchor=N, command=no_button)
no_button.grid(row=1, column=0)

yes_image = PhotoImage(file='./images/right.png')
yes_button = Button(image=yes_image, highlightthickness=0, bd=0, command=yes_button)
yes_button.grid(row=1, column=1)

#-------------------CANVAS------------------------#

canvas = Canvas(width=900, height=626, bg='#B1DDC6', highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
front_image_spanish = PhotoImage(file='./images/card_front.png')
front_image_polish = PhotoImage(file='./images/card_back.png')
image_canvas = canvas.create_image(50,50,image=front_image_spanish, anchor=NW)
canvas_title = canvas.create_text(450, 200, text="", font=("Ariel", 40, "italic"), fill="black")
canvas_item = canvas.create_text(450, 350, text="", font=("Ariel", 60, "bold"), fill="black")


next_card()

window.mainloop()
