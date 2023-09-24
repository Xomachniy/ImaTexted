from pygame import *
from random import randint
init()
mixer.init()

window = display.set_mode((900, 600))
display.set_caption('ImaTexted')

Plain = transform.scale(image.load('Plain.jpg'), (900, 600))
Forest = transform.scale(image.load('Forest.jpg'), (900, 600))

clock = time.Clock()
fps = 60

game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(Plain, (0, 0))

    clock.tick(fps)
    display.update()