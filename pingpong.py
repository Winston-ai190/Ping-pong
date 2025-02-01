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

back = (200, 225, 225)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60
ball = GameSprite('ball1.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        ball.reset()

    display.update()
    clock.tick(FPS)