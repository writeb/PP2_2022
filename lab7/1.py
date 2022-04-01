import pygame
import os
import datetime
pygame.init()
screen = pygame.display.set_mode((1440,900))
#pygame.display.set_caption('Program 1')
image = ['clock.png', 'ruka2.png', 'ruka1.png']

if image[0] is None:
    for i in image:
        i = i.replace('/', os.sep).replace('\\', os.sep)
clock = pygame.image.load(image[0])
second = pygame.image.load(image[1])
minute = pygame.image.load(image[2])
done = False



while not done:
    screen.fill((255,255,255))
    screen.blit(clock,(0,0))
    now = datetime.datetime.now()
    second_rotate = pygame.transform.rotate(second, -6*now.second + 60)
    minute_rotate = pygame.transform.rotate(minute, -6 * now.minute - 50)
    rect_second = second_rotate.get_rect(center = second.get_rect(center = (637,481)).center)
    rect_minute = minute_rotate.get_rect(center = minute.get_rect(center = (655,555)).center)
    screen.blit(second_rotate, rect_second)
    screen.blit(minute_rotate, rect_minute)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True