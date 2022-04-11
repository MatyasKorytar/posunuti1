led.plot(0, 0)
led.plot(0, 1)
led.plot(0, 2)
led.plot(0, 3)
led.plot(0, 4)
def on_button_pressed_a():
    y = 0
    x = 0
    while y < 5:
        basic.clear_screen()
        led.plot(x, 0)
        led.plot(x, 1)
        led.plot(x, 2)
        led.plot(x, 3)
        led.plot(x, 4)
        x += 1
        basic.pause(3000)
        y += 1 
input.on_button_pressed(Button.A, on_button_pressed_a)
