import pygame
import random
import time

pygame.init()
speed = 15
running = True
FPS = pygame.time.Clock()
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

window_width = 900
window_height = 600

pygame.display.set_caption('Snake game')
screen = pygame.display.set_mode((window_width, window_height))
 
# Первоначальное место змеим
snake_position = [100, 50]
# 3 блока змеи
snake_body = [[100,50], [90,50], [80,50]]

fruit_position = [random.randrange(1, (window_width//10)) * 10,
				random.randrange(1, (window_height//10)) * 10]
fruit = True

# Дефолтное направление змеи
direction = 'RIGHT'
change_to = direction
score = 0
level = 1

def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)                            # Создаем объект шрифта
	score_surface = score_font.render('Score : ' + str(score), True, color) # Создаем отображение очков
	score_rect = score_surface.get_rect()                                   # Создаем прямоугольник как место для цифры
	score_rect.topleft = (window_width - 890, window_height - 600)
	screen.blit(score_surface, score_rect)                             # Отображаем текст

def show_level(choice, color, font, size):
	level_font = pygame.font.SysFont(font, size)
	level_surface = level_font.render('Level : ' + str(level), True, color)
	level_rect = level_surface.get_rect()
	level_rect.topright = (window_width - 10, window_height - 600)
	screen.blit(level_surface, level_rect)

def game_over():
	game_font = pygame.font.SysFont('times new roman', 50)                              # Создаем поверхность где будет написан текст
	game_over_surface = game_font.render('Your Score is : ' + str(score), True, RED)    # Прямоугольник для поверхности текста
	game_over_surface2 = game_font.render('Your Max Level is : ' + str(level), True, RED)
	game_over_rect = game_over_surface.get_rect()                                       # Устанавливаем позицию текста
	game_over_rect.midtop = (window_width/2, window_height/4)                           # blit нарисует текст на экране
	game_over_rect2 = game_over_surface2.get_rect()
	game_over_rect2.midtop = (window_width/2, window_height - 500)
	screen.blit(game_over_surface, game_over_rect)
	screen.blit(game_over_surface2, game_over_rect2)
	pygame.display.flip()
	time.sleep(3)
	pygame.quit()
	quit()

# Главная функция
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	if change_to == 'UP' and direction != 'DOWN':               # Благодаря этим условиям змея не будет двигаться резко 
		direction = 'UP'                                        # в противоположную сторону
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Если фрукт и змея столкнутся очки увеличатся на 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 1
		fruit = False
		if score % 3 == 0:
			level += 1
			speed += 5
	else: snake_body.pop()
	if not fruit:
		fruit_position = [random.randrange(1, (window_width//10)) * 10,
						random.randrange(1, (window_height//10)) * 10]
	fruit = True
	
	screen.fill(BLACK)
	
	for pos in snake_body:
		pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(screen, RED, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))  # создаем яблоко в виде прямоугольника
    # Условия game_over
	if snake_position[0] < 0 or snake_position[0] > window_width-10: game_over()
	if snake_position[1] < 0 or snake_position[1] > window_height-10: game_over()
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]: game_over()

	show_score(1, WHITE, 'times new roman', 20)
	show_level(1, WHITE, 'times new roman', 20)

	pygame.display.update()

	FPS.tick(speed)