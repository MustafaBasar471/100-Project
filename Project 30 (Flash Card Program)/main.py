from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

card = {}
to_learn = {}

try:
    data = pandas.read_csv("./Project 30 (Flash Card Program)/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Project 30 (Flash Card Program)/data/English_Words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_word():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card =random.choice(to_learn)
    canvas.itemconfig(title_canvas, text="English", fill="black")
    canvas.itemconfig(word_canvas, text=card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    global card
    canvas.itemconfig(title_canvas, text="Turkish", fill="white")
    canvas.itemconfig(word_canvas, text=card["Turkish"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_true():
    to_learn.remove(card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./Project 30 (Flash Card Program)/data/words_to_learn.csv", index=False)
    new_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="./Project 30 (Flash Card Program)/image/card_front.png")
card_back_img = PhotoImage(file="./Project 30 (Flash Card Program)/image/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_canvas = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

f_image = PhotoImage(file="./Project 30 (Flash Card Program)/image/wrong.png")
f_button = Button(image=f_image, highlightthickness=0, command=new_word)
f_button.grid(row=1, column=0)

t_image = PhotoImage(file="./Project 30 (Flash Card Program)/image/right.png")
t_button = Button(image=t_image, highlightthickness=0, command=is_true)
t_button.grid(row=1, column=1)

new_word()
window.mainloop()