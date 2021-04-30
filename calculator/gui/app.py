from tkinter import Tk, Label

from calculator.settings import WINDOW_SIZE, WINDOW_BUTTONS, WINDOW_TITLE
from calculator.gui import render_buttons


app = Tk()
app["bg"] = "#000"
app.geometry(WINDOW_SIZE)
app.title(WINDOW_TITLE)
app.resizable(False, False)

app_expr = Label(text='', font=("Consolas", 21, "bold"), bg="#000", foreground="#FFF")
app_expr.place(x=11, y=50)

app_err = Label(text='', font=("Consolas", 10, "bold"), bg="#000", foreground="#de4c47")
app_err.place(x=11, y=92)

app_buttons = render_buttons(WINDOW_BUTTONS)
