from calculator.gui import app_expr, app_err, render_label_text


def button_click_event(button):
    try:
        render_label_text(app_err, "", "")
        button_value = button["text"]
        expr_value = app_expr["text"]
        if button_value == "C":
            expr_value = ""
        elif button_value == "=":
            expr_value = str(eval(expr_value))
        elif button_value == "DEL":
            expr_value = expr_value[0:len(expr_value) - 1]
        else:
            if expr_value == "0":
                expr_value = ""
            expr_value += button_value
        render_label_text(app_expr, expr_value, "")
    except Exception as e:
        render_label_text(app_err, str(e), "")
        render_label_text(app_expr, "", "")


def append_click_event(button):
    button.configure(command=lambda: button_click_event(button))
