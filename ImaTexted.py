from pygame import *
from random import randint
init()
mixer.init()

window = display.set_mode((900, 600))
display.set_caption('ImaTexted')

Plain = transform.scale(image.load('Plain.jpg'), (900, 600))
Forest = transform.scale(image.load('Forest.jpg'), (900, 600))
Tavern = transform.scale(image.load('Tavern.jpg'), (900, 600))
Plain2 = transform.scale(image.load('Plain2.jpg'), (900, 600))
City = transform.scale(image.load('City.jpg'), (900, 600))

mixer.init()
mixer.music.load('In-tavern.ogg')
mixer.music.play()

clock = time.Clock()
fps = 60

game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if e.type == KEYDOWN:
        if e.key == K_1:
            window.blit(Tavern, (0, 0))
            mixer.music.load('In-tavern.ogg')
            mixer.music.play()
        if e.key == K_2:
            window.blit(Forest, (0, 0))
            mixer.music.load('ForestBoss.ogg')
            mixer.music.play()
        if e.key == K_3:
            window.blit(Plain, (0, 0))
            mixer.music.load('Memory.ogg')
            mixer.music.play()
        if e.key == K_4:
            window.blit(Plain2, (0, 0))
            mixer.music.load('Trigger.ogg')
            mixer.music.play()
        if e.key == K_5:
            window.blit(City, (0, 0))
            mixer.music.load('City.ogg')
            mixer.music.play()

    clock.tick(fps)
    display.update()