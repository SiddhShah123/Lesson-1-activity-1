import pygame
import random
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
PLAYER_START_Y = 370
PLAYER_START_X = 380
PLAYER_MOVEMENT_SPEED = 5
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
FONT_SIZE = 72

pygame.init()
bg_image = pygame.transform.scale(pygame.image.load("game_background.png"),(SCREEN_WIDTH,SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Player Catch the Enemy")
font = pygame.font.SysFont("Times New Roman",FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,image,width,height):
        super().__init__()
        loaded_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(loaded_image, (width, height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)  

sprite1 = Sprite("cat.png",50,50)
sprite1.rect.x,sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)

one_sprite = pygame.sprite.Group()
sprites_group = pygame.sprite.Group()

one_sprite.add(sprite1) 

for i in range (7):
    sprite2 = Sprite("mouse.png",30,30)
    sprite2.rect.x,sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
    sprites_group.add(sprite2) 

score_value = 0 

running, won = True,False
clock = pygame.time.Clock()
while running :
    screen.blit(bg_image,(0,0))    
    one_sprite.draw(screen)
    sprites_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won :
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_MOVEMENT_SPEED
        sprite1.move(x_change, y_change)
        hits = pygame.sprite.spritecollide(sprite1, sprites_group, True)
        for hit_item in hits:
            one_sprite.remove(hit_item)
            score_value = score_value + 1  
            if score_value == 7:
                won = True
    if won :
            win_text = font.render("You win!", True, pygame.Color('black'))
            screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
            (SCREEN_HEIGHT - win_text.get_height()) // 2))    

    pygame.display.flip()
    clock.tick(90)

pygame.quit() 
