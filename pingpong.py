from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

back = (200, 225, 225)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60
ball = GameSprite('ball1.png', 200, 200, 4, 50, 50)

racket1 = Player('platform1.png', 30, 200, 10, 10, 100)
racket2 = Player('platform1.png', 520, 200, 10, 10, 100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        ball.reset()
        racket1.reset()
        racket2.reset()
    display.update()
    clock.tick(FPS)
