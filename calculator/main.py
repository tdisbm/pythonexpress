from calculator.gui import app, app_buttons
from calculator.event import append_click_event

for button in app_buttons:
    append_click_event(button)

app.mainloop()
