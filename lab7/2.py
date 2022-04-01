import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))

running = True
_currently_playing_song = None
clock = pygame.time.Clock()
#music download
# pygame.display.set_caption('Muisic Player v1.0')

#text
font = pygame.font.Font(None,25)
#text

songs = ['music.mp3', 'music2.mp3', 'music3.mp3']

while running:
    name = font.render("Runaway",True,(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
            pygame.mixer.music.load(songs[1])
            pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
            pygame.mixer.music.load(songs[2])
            pygame.mixer.music.play(0)    
            
              
                
                
    screen.fill((0,90,100))
    #desing
    pygame.draw.rect(screen, (0, 0, 0), (30, 50, 240, 30), 1)
    pygame.draw.rect(screen, (0, 0, 0), (30, 90, 240, 30), 1)
    pygame.draw.rect(screen, (0, 0, 0), (30, 130, 240, 30), 1)
    pygame.draw.rect(screen, (0, 0, 0), (30, 170, 115, 30), 1)
    pygame.draw.rect(screen, (0, 0, 0), (150, 170, 120, 30), 1)
    #text 
    
    maintext = font.render("MP3 Player",True,(0,0,0))
    ptext = font.render("PLAY",True,(0,0,0))
    stext = font.render("STOP",True,(0,0,0))
    ntext = font.render("NEXT",True,(0,0,0))
    prtext = font.render("PREVIOUS ",True,(0,0,0))
    screen.blit(maintext,(110,20))
    screen.blit(name,(110,55))
    screen.blit(ptext,(130,95))
    screen.blit(stext,(130,135))
    screen.blit(prtext,(40,175))
    screen.blit(ntext,(180,175))
    #text
    pygame.display.update()
    clock.tick(60)
pygame.quit()


'''
Instruction
space - play music
e - stop music
r_shift - previous music
l_shift - next music
'''