import pygame
from pygame.locals import *
import random
import psycopg2

pygame.init()

conn = psycopg2.connect(
    host = 'localhost',
    database = 'snake',
    port = '5432',
    user = 'snake_user',
    password = 'Kaktusbro228'
)
cursor = conn.cursor()



#creating display
screen = pygame.display.set_mode((600, 300))
screen.fill((46, 180, 201))
w, h = screen.get_size()



#general class for snake
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coordinates = [[x, y]]
        self.radius = 10
        self.size = 1
        self.dy = -1
        self.dx = 0
        self.add = False
        self.speed = 100
    def draw(self):
        for coord in self.coordinates:
            pygame.draw.circle(screen, (100, 255, 0), coord, self.radius)
    def adding(self):
        self.size += 1
        self.coordinates.append([0, 0])
        self.add = False

    def move(self):
        if self.add:
            self.adding()
        for i in range(self.size-1, 0, -1):
            self.coordinates[i][0] = self.coordinates[i-1][0]
            self.coordinates[i][1] = self.coordinates[i-1][1]
        
        self.coordinates[0][0] += self.dx
        self.coordinates[0][1] += self.dy
    def eat(self, food_x, food_y, stage):
        x = self.coordinates[0][0]
        y = self.coordinates[0][1]
        if stage % 5 == 0:
            self.speed += 0.01
        if food_x - 15 <= x <= food_x + 15 and food_y - 15 <= y <= food_y + 15:
            return True
        return False
    def self_collision(self):
        return self.coordinates[0] in self.coordinates[1:]
    # wall collision
    def wall_collision(self, stage):
        if 195 < self.coordinates[0][0] < 215+150+stage*5 and 85 < self.coordinates[0][1] < 105+105+stage*5:
            return True
        return False

# general class for food
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(5, 595)
        self.y = random.randint(5, 295)
    #generating position for food
    def gen(self, stage):
        self.x = random.randint(5, 595)
        self.y = random.randint(5, 295)
        if 195 < self.x < 215+150+stage*5 and 85 < self.y < 105+105+stage*5:
            while 195 < self.x < 215+150+stage*5 or 85 < self.y < 105+105+stage*5:
                self.x = random.randint(5, 595)
                self.y = random.randint(5, 295)  
    def draw(self):
        pygame.draw.circle(screen, (23, 23, 23), (self.x, self.y), 8)
    
    


snake = Snake(550, 210)



food = Food()
#step = dx and dy
step = 1

#controlling speed
clock = pygame.time.Clock()

pressed = pygame.key.get_pressed()
points = 0
done = False
level = 1
level_add = False
a, b, c = 33, 120, 40
name = input()

sql = "select exists(select 1 from snakedata where name=%s)"
cursor.execute(sql, (name,))
ans = cursor.fetchone()
if(ans[0]):
    sql = "select level from snakedata where name = %s"
    cursor.execute(sql, (name,))
    t = cursor.fetchone()
    level = t[0]
else:
    sql = "insert into snakedata (name, level) values(%s, %s);"
    cursor.execute(sql, (name, level))
    conn.commit()




#main code
while not done:
    clock.tick(snake.speed)
    screen.fill((46, 180, 201))
    pygame.draw.rect(screen, (a, b, c), (205, 95, 150+level*5, 105+level*5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not snake.dy == step:
                snake.dx = 0
                snake.dy = -step
            if event.key == pygame.K_s and not snake.dy == -step:
                snake.dx = 0
                snake.dy = step
            if event.key == pygame.K_a and not snake.dx == step:
                snake.dx = -step
                snake.dy = 0
            if event.key == pygame.K_d and not snake.dx == -step:
                snake.dx = step
                snake.dy = 0
            if event.key == pygame.K_SPACE:
                snake.speed -= 1
            if event.key == pygame.K_LSHIFT:
                snake.speed += 1
    #score
    pat = pygame.font.Font(None, 35)
    lvl = pat.render('Level: '+str(level), True, (255, 255, 255))
    text = pat.render('Score: '+str(points), True, (255, 255, 255))
    screen.blit(text, (0, 0))
    screen.blit(lvl, (490, 0))
  
  
    if snake.eat(food.x, food.y, level):
        a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        #levels and increasing speed
        points += 10
        if points % 20 == 0:
            level_add = True
        snake.speed += 1
        snake.add = True
        food.gen(level)

        if level_add:
            level += 1
            level_add = False

        if [food.x, food.y] in snake.coordinates:
            while not [food.x, food.y] in snake.coordinates:
                food.gen(level)

        
    

    snake.move()
    snake.draw()
    food.draw()
    #leaving play area
    if snake.coordinates[0][0] > 600:
      snake.coordinates[0][0] = 0
    if snake.coordinates[0][0] < 0:
      snake.coordinates[0][0] = 600
    if snake.coordinates[0][1] > 300:
      snake.coordinates[0][1] = 0
    if snake.coordinates[0][1] < 0:
      snake.coordinates[0][1] = 300 
    #game over situations
    if snake.self_collision() or snake.wall_collision(level):
        temp = pygame.font.Font(None, 100)
        over = temp.render('Game over', True, (255, 0, 255))
        
        while not done:
            screen.blit(over, (100, 100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


    
    pygame.display.flip()

    
sql = """
    update snakedata
    set level = %s
    where name = %s;
    """
cursor.execute(sql, (level, name))
conn.commit()

pygame.quit()