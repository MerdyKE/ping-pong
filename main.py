from pygame import *

WIDTH, HEIGHT = 500, 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('пинг понг')
window_color = (100, 150, 250)

class GameSprite(sprite.Sprite):
    def __init__(self, speed, x, y, x1, y1 ):
        super().__init__()
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x1 = x1
        self.y1 = y1

class Player(GameSprite):

    def update( self ):
        keys = key.get_pressed()
        if keys[ K_w ] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[ K_s ] and self.rect.y < HEIGHT - 70:
            self.rect.y += self.speed



game = True

clock = time.Clock()
FPS = 60

while game:


    for e in event.get():

        if e.type == QUIT:
            game = False

    window.fill(window_color)
    display.update()
    clock.tick(FPS)
