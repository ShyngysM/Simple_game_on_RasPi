from gpiozero import Button
from gpiozero import LEDBoard

buttonL = Button(2)
buttonR = Button(3)

leds = LEDBoard(5, 6, 13, 19)
previous_state = 1
current_state = 0
x = 0
while True:
    leds[x].on()
    if buttonL.is_pressed:
        print("Button L is pressed")
        if previous_state != current_state:
            if x != 3:
                x += 1  
                print("moved right", x)
                leds[x-1].off()
                current_state = previous_state
            else:
                x = 3
    elif buttonR.is_pressed:
        print("Button R is pressed")
        if previous_state != current_state:
            if x != 0:
                x -= 1  
                print("moved left", x)
                leds[x+1].off()
                current_state = previous_state
            else:
                x = 0
    else:
        current_state = 0
