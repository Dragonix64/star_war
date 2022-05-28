
from pygame import*

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


init()
window = display.set_mode((500, 700))
display.set_caption("Стрелялка")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > - 60:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 250:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -10)
        bullets.add(bullet)
            
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Enemy(sprite.Sprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randit(80, win_widtg - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()



display.set_caption("Maze")
game = True
finish = False
clock = time.Clock()
FPS = 60
background = transform.scale(image.load('galaxy.jpg'), (500, 700))
win_width = 700

player = Player('rocket.png', 200, 550, 80, 100, 30)
bullets = sprite.Group()
game = True
while game is True:
    for ev in event.get():
        if ev.type == QUIT:
            game = False

        elif ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                fire_sound.play()
                player.fire()
        



    if finish != True:
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        text = font2.render('Счет: ' + str(score), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        monsters.update()





        monsters.draw(window)
        bullets.update()
        bullets.draw(window)








    display.update()
    clock.tick(FPS)