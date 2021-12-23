def on_button_pressed_a():
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_arrow(ArrowNames.WEST)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_arrow(ArrowNames.EAST)
input.on_button_pressed(Button.B, on_button_pressed_b)
