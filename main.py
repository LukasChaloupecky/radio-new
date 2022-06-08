manual = True

def on_pin_pressed_p1():
    radio.send_number(5)
    images.create_image("""
    # . # . #
    . . . . .
    # . # . #
    . . . . .
    # . # . #
    """).show_image(0)
    if manual:
        manual = False
    else:
        manual = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_button_pressed_a():
    images.create_image("""
        . . . . .
                . # . . .
                # # # # #
                . # . . .
                . . . . .
    """).show_image(0)
    radio.send_number(2)

def on_button_pressed_ab():
    radio.send_number(0)
    images.create_image("""
    . . # . .
    . # # # .
    . . # . .
    . . # . .
    . . # . .
    """).show_image(0)
                             
    

def on_button_pressed_b():
    radio.send_number(3)
    images.create_image("""
        . . . . .
                . . . # .
                # # # # #
                . . . # .
                . . . . .
    """).show_image(0)

def on_pin_pressed_p0():
    radio.send_number(1)
    images.create_image("""
    . . # . .
    . . # . .
    . . # . .
    . # # # .
    . . # . .
    """).show_image(0)

radio.set_group(77)
def on_forever():
    if manual:
        input.on_button_pressed(Button.B, on_button_pressed_b)
        input.on_button_pressed(Button.AB, on_button_pressed_ab)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

basic.forever(on_forever)