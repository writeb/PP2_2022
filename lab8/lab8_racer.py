import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
FPS = pygame.time.Clock()
speed = 5
score = 0
coins = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

screen_x, screen_y = 400, 600
pygame.display.set_caption('Racer')
screen = pygame.display.set_mode((screen_x,screen_y))
screen.fill((WHITE))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_x - 40), 0)
    
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_x - 40), 0)  # 0 означает на оси X
    
class Player(pygame.sprite.Sprite):         # Передача pygame.sprite.Sprite в параметры делает класс игрока дочерним классом.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        # Функция get_rect() - способна автоматически создавать прямоугольник того же размера, что и изображение. 
        # Мы будем использовать это в обнаружении столкновений
        self.rect = self.image.get_rect()   
        # self.rect.center - определяет начальную позицию Rect. Позже мы будем использовать 
        # координаты прямоугольника, чтобы нарисовать изображение в том же самом месте.
        self.rect.center = (160, 550)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5) 
        if self.rect.left > 0:
              if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < screen_x:        
              if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                # x, y directions 
                  self.rect.move_ip(5, 0)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_x - 40), 0)
    def spawn(self):
        self.rect.center = (random.randint(40, screen_x - 40), 0)


    def move(self):
        global coins
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_x - 40), 0)
    
P1 = Player()
E1 = Enemy()
C1 = Coins()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_objet = pygame.sprite.Group()
coins_objet.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
# Затем мы используем функцию set_timer() модуля времени Pygame для вызова объекта 
# события INC_SPEED каждые 1000 миллисекунд или 1 секунду.
pygame.time.set_timer(INC_SPEED, 1000)

def show_coins(choice, color, font, size):
    coins_font = pygame.font.SysFont(font,size)
    coins_surface = coins_font.render('Coins : ' + str(coins), True, color)
    coins_rect = coins_surface.get_rect()
    coins_rect.topright = (screen_x - 10, screen_y - 600)
    screen.blit(coins_surface, coins_rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            speed += 0.05
    
    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, BLACK)
    screen.blit(scores, (10,10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(P1, coins_objet):
        coins+=1
        C1.spawn()
        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):    # Эта функция returns True если есть collsion между объектом и группой объектов
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(2)

        screen.fill(RED)
        screen.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    show_coins(1, BLACK, 'Verdana', 20)
    pygame.display.update()
    FPS.tick(60)