import pygame
pygame.init()

WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
PINK = (255,105,180)
PURPLE = (134,1,175)
TURQUOISE =(64,224,208)
BLACK = (0,0,0)
 
score = 0
lives = 3

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ice Breaker")

import pygame
pygame.init()
 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
PINK = (255,105,180)
PURPLE = (134,1,175)
TURQUOISE =(64,224,208)
BLACK = (0,0,0)

 
score = 0
lives = 3
 
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ice Breaker")
 
carryOn = True
 
clock = pygame.time.Clock()
 
while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False  

   
    screen.fill(PINK)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    pygame.display.flip()
     
    clock.tick(60)



#PADDLE STARTS
    
import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()

from paddle import Paddle

paddle= Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x= 350
paddle.rect.y= 560

import pygame
from paddle import Paddle
 
pygame.init()
 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
 
score = 0
lives = 3
 
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
 
all_sprites_list = pygame.sprite.Group()
 
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 
all_sprites_list.add(paddle)
 
carryOn = True
 
clock = pygame.time.Clock()
 
while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False  
    all_sprites_list.update()
 

    screen.fill(PINK)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    all_sprites_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
         
