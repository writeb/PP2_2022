import pygame
pygame.init()

screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
FPS = 50
WHITE = (255,255,255)
GREEN = (0,255,0)
running = True

x = 0
y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 25
    if pressed[pygame.K_LEFT]: x -= 25 
    if pressed[pygame.K_RIGHT]: x += 25
    if pressed[pygame.K_DOWN]: y += 25

    if x + 25 >= 700:
        x = 620
    if x - 25 <= 0:
       x = 30
    if y + 25 >= 700:
        y = 620
    if y - 25 <= 0:
        y = 30

    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, (x,y), 25)

    pygame.display.flip()
    clock.tick(FPS)