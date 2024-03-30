from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

run = True
clock = time.Clock()
FPS = 60
speed = 10

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)

