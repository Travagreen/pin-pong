from pygame import *
window = display.set_mode((700,500))

display.set_caption('ПинПонг')
clock = time.Clock()
backgroun = transform.scale(image.load(),(700,500)

while Game():
    for e in event.get():
        if e.type == QUIT:
            game == False:

    display.uptade()
    clock.tick(60)
