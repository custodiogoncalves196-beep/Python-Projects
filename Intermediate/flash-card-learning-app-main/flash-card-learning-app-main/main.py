from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
flip_timer = None


# -------------------- DATA -------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")


# -------------------- FUNCTIONS -------------------- #

def game():
    global current_card, flip_timer

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)

    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def known_card():
    data_dict.remove(current_card)

    words_to_learn = pandas.DataFrame(data_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)

    game()


# -------------------- UI -------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

canvas = Canvas(
    window,
    width=860,
    height=700,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(440, 290, image=front_image)

title_text = canvas.create_text(
    400,
    150,
    text="French",
    font=("Arial", 40, "italic")
)

word_text = canvas.create_text(
    400,
    263,
    text="Word",
    font=("Arial", 40, "bold")
)

canvas.grid(row=0, column=0)


# Wrong button

wrong_image = PhotoImage(file="images/wrong.png")

wrong_button = Button(
    image=wrong_image,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    command=game
)

canvas.create_window(250, 620, window=wrong_button)


# Right button

right_image = PhotoImage(file="images/right.png")

right_button = Button(
    image=right_image,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    command=known_card
)

canvas.create_window(610, 620, window=right_button)


game()

window.mainloop()