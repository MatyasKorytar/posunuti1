led.plot(0, 0)
led.plot(1, 0)
led.plot(2, 0)
led.plot(3, 0)
led.plot(4, 0)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let y = 0
    let x = 0
    while (y < 5) {
        basic.clearScreen()
        led.plot(0, x)
        led.plot(1, x)
        led.plot(2, x)
        led.plot(3, x)
        led.plot(4, x)
        x += 1
        basic.pause(3000)
        y += 1
    }
})
