let manual = true
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    let manual: boolean;
    radio.sendNumber(5)
    images.createImage(`
    # . # . #
    . . . . .
    # . # . #
    . . . . .
    # . # . #
    `).showImage(0)
    if (manual) {
        manual = false
    } else {
        manual = true
    }
    
})
radio.setGroup(77)
basic.forever(function on_forever() {
    if (manual) {
        input.onButtonPressed(Button.B, function on_button_pressed_b() {
            radio.sendNumber(3)
            images.createImage(`
        . . . . .
                . . . # .
                # # # # #
                . . . # .
                . . . . .
    `).showImage(0)
        })
        input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
            radio.sendNumber(0)
            images.createImage(`
    . . # . .
    . # # # .
    . . # . .
    . . # . .
    . . # . .
    `).showImage(0)
        })
        input.onButtonPressed(Button.A, function on_button_pressed_a() {
            images.createImage(`
        . . . . .
                . # . . .
                # # # # #
                . # . . .
                . . . . .
    `).showImage(0)
            radio.sendNumber(2)
        })
        input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
            radio.sendNumber(1)
            images.createImage(`
    . . # . .
    . . # . .
    . . # . .
    . # # # .
    . . # . .
    `).showImage(0)
        })
    }
    
})
