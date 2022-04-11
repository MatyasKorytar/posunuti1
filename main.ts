led.plot(0, 0)
led.plot(0, 1)
led.plot(0, 2)
led.plot(0, 3)
led.plot(0, 4)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let y = 0
    let x = 0
    while (y < 5) {
        basic.clearScreen()
        led.plot(x, 0)
        led.plot(x, 1)
        led.plot(x, 2)
        led.plot(x, 3)
        led.plot(x, 4)
        x += 1
        basic.pause(3000)
        y += 1
    }
})
