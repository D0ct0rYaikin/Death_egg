#Создай собственный Шутер!
from pygame import *
from random import *
from time import sleep

mixer.init()
mixer.music.load('space.ogg')
vzryv = mixer.Sound('vzryv.ogg')
font.init() 
Lost = 0   
point = 0   
amo = 0
font1 = font.Font(None, 100)
font2 = font.Font(None, 40)
font3 = font.Font(None, 40)
win = font1.render('YOU WIN', True, (0, 255, 0))
lose = font1.render('YOU LOSE', True, (255, 0, 0))
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, x_size, y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x_size, y_size))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 1366:
            self.rect.x += self.speed
    def bulelet_creat(self):
        sprite_center_x = self.rect.centerx
        sprite_top = self.rect.top
        bullet = Bullet('egg.png', sprite_center_x, sprite_top, 15, 10, 10)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global Lost
        if self.rect.y >= 700:
            Lost += 1
            self.rect.x = 683
            start_x = randint(-633, 633)
            self.rect.y = 0
            self.rect.x == start_x


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


amo = 0
FPS = 60
x2 = 683
x3 = 100
x4 = 300
x5 = 800
x6 = 1000
y1 = 600
x1 = 100
y2 = 0
x8 = 700
hero = Hero('rocket.png', x1, y1, 30, 65, 65)
enemy1 = Enemy('ufo.png', x3, y2, 4, 65, 65)
enemy2 = Enemy('ufo.png', x2, y2, 5, 65, 65)
enemy3 = Enemy('ufo.png', x4, y2, 6, 65, 65)
enemy4 = Enemy('ufo.png', x5, y2, 7, 65, 65)
enemy5 = Enemy('ufo.png', x6, y2, 8, 65, 65)
asteroid = Enemy('asteroid.png', x8, y2, 3, 65, 65)
enemys = sprite.Group()
enemys.add(enemy1)
enemys.add(enemy2)
enemys.add(enemy3)
enemys.add(enemy4)
enemys.add(enemy5)
bullets = sprite.Group()
asteroids = sprite.Group()
asteroids.add(asteroid)
window = display.set_mode((1366, 700))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (1366, 768))
clock = time.Clock()

finish = False
game = True
while game:
    points = font3.render ('Очки: ' + str(point), True, (255, 255, 255))
    lost = font2.render('Пропущенные враги: ' + str(Lost), True, (255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                vzryv.play()                
                hero.bulelet_creat()
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        window.blit(lost, (50, 50))
        window.blit(points, (50, 100))
        hero.move()
        enemys.update()
        if sprite.spritecollide(hero, enemys, True):
            window.blit(lose, (500, 350))
            vzryv.play()
            ghj = randint(-633, 633)
            x7 = 683 + ghj
            speed = randint(4, 8)
            enemy = Enemy('ufo.png', x7, y2, speed, 65, 65)
            enemys.add(enemy)
            finish = True
        if sprite.groupcollide(bullets, enemys, True, True):
            vzryv.play()
            point += 1
            ghj = randint(-633, 633)
            x7 = 683 + ghj
            speed = randint(4, 8)
            enemy = Enemy('ufo.png', x7, y2, speed, 65, 65)
            enemys.add(enemy)
        if sprite.spritecollide(hero, asteroids, True):
            window.blit(lose, (500, 350))
            vzryv.play()
            ghj = randint(-633, 633)
            x7 = 683 + ghj
            asteroid = Enemy('asteroid.png', x7, y2, 3, 65, 65)
            asteroids.add(asteroid)
            finish = True
        if sprite.groupcollide(bullets, asteroids, True, False):
            vzryv.play()                
        enemys.draw(window)
        asteroids.draw(window)
        asteroids.update()
        bullets.update()
        bullets.draw(window)
        display.update()
        clock.tick(FPS)
    elif finish == True:
        sleep(5)
        finish = False
        point = 0
        Lost = 0





