led.plot(0, 0)
led.plot(1, 0)
led.plot(2, 0)
led.plot(3, 0)
led.plot(4, 0)
def on_button_pressed_a():
    y = 0
    x = 0
    while y < 5:
        basic.clear_screen()
        led.plot(0, x)
        led.plot(1, x)
        led.plot(2, x)
        led.plot(3, x)
        led.plot(4, x)
        x += 1
        basic.pause(3000)
        y += 1 
input.on_button_pressed(Button.A, on_button_pressed_a)
