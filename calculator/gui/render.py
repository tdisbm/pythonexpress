from tkinter import Button


def render_buttons(button_titles):
    offset_x, offset_y = 10, 140
    buttons = []
    for title in button_titles:
        button = Button(text=title, bg="#FFF", font=("Consolas", 15))
        button.place(x=offset_x, y=offset_y, width=115, height=79)
        buttons.append(button)
        offset_x += 117
        if offset_x > 400:
            offset_x = 10
            offset_y += 81
    return buttons


def render_label_text(label, text, text_default="0"):
    text_to_update = text
    if not text:
        text_to_update = text_default or ""
    label.configure(text=text_to_update)
