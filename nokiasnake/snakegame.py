import sys
import random
import pygame  
from pygame.math import Vector2 
pygame.init()


title_font = pygame.font.Font(None,60)
score_font = pygame.font.Font(None,30)
credits_font = pygame.font.Font(None,30)


GREEN = (170, 200, 90)
DARK_GREEN = (40, 50, 20)

CELL_SIZE = 30
NUMBER_OF_CELLS = 25
OFFSET = 75

class Food:
    def __init__(self,snake_body):
        self.position = self.generate_random_pos(snake_body)

    def draw(self):
        food_rect = pygame.Rect(OFFSET + self.position.x*CELL_SIZE,OFFSET + self.position.y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
        screen.blit(food_surface,food_rect)

    def generate_random_cell(self):
        x = random.randint(0,NUMBER_OF_CELLS -1)
        y = random.randint(0,NUMBER_OF_CELLS -1)
        return Vector2(x,y)

    def generate_random_pos(self,snake_body):
        position = self.generate_random_cell()             
        while position in snake_body:
            position = self.generate_random_cell()
        return position

class Snake:    
    def __init__(self):
        self.body = [Vector2(6,8),Vector2(5,8),Vector2(4,8)]
        self.direction = Vector2(1,0)
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound("sounds/eat.mp3")
        self.wall_hit_sound = pygame.mixer.Sound("sounds/cancel.mp3")


    def draw(self):
        for segment in self.body:
            segment_rect = pygame.Rect(OFFSET + segment.x*CELL_SIZE,OFFSET + segment.y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,DARK_GREEN,segment_rect,0,7)
    def update(self):
        self.body.insert(0,self.body[0]+self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
             self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6,8),Vector2(5,8),Vector2(4,8)]
        self.direction = Vector2(1,0)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "Running"
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw()
    def update(self):
        if self.state == "Running":
            self.snake.update()
            self.check_collision_with_food()   
            self.collision_with_edges()
            self.check_collision_with_tail()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score += 1
            self.snake.eat_sound.play()

    def collision_with_edges(self):
        if self.snake.body[0].x == NUMBER_OF_CELLS or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == NUMBER_OF_CELLS or self.snake.body[0].y == -1:
            self.game_over()
   
    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "Stopped"
        self.score = 0
        self.snake.wall_hit_sound.play()

    def check_collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()


screen = pygame.display.set_mode((2*OFFSET + CELL_SIZE*NUMBER_OF_CELLS,2*OFFSET + CELL_SIZE*NUMBER_OF_CELLS))
pygame.display.set_caption("nokia snake")
clock = pygame.time.Clock()
game = Game() 
food_surface = pygame.image.load("snake/egg.png")
food_surface = pygame.transform.scale(food_surface, (CELL_SIZE,CELL_SIZE))
snake_update = pygame.USEREVENT
pygame.time.set_timer(snake_update,200)

while True:
    for event in pygame.event.get():
        if event.type == snake_update:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.state == "Stopped":
                game.state = "Running"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0,-1) 
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2(-1,0)

    #drawing
    screen.fill(GREEN)
    pygame.draw.rect(screen,DARK_GREEN,
                     (OFFSET-5 ,OFFSET-5 ,CELL_SIZE*NUMBER_OF_CELLS+10,CELL_SIZE*NUMBER_OF_CELLS+10),5)
    game.draw()

    score_surface = score_font.render("score:"+str(game.score),True,DARK_GREEN)
    screen.blit(score_surface,(OFFSET+670,50))

    title_surface = title_font.render("NOKIA SNAKE",True,DARK_GREEN)
    screen.blit(title_surface,(OFFSET+227,20))

    credits_surface = credits_font.render("by@garvit33",True,DARK_GREEN)
    screen.blit(credits_surface,(OFFSET+10,40))

    pygame.display.update()
    clock.tick(60)