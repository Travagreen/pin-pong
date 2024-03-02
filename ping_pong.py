from pygame import *
window = display.set_mode((700,500))

display.set_caption('ПинПонг')
clock = time.Clock()
backgroun = transform.scale(image.load('background.png'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self,filename,x,y,width,height,speed):
        super().__init__()
        self.image = transform.scale(image.load(filename),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    pass
ball = GameSprite('шарык.png',20,30,40,20,10)
clock = time.Clock()
game = True
finish = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game == False

    display.update()
    clock.tick(60)
