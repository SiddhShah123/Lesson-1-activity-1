import pygame
import random
import math
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PLAYER_START_Y = 700
PLAYER_START_X = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4 
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLSION_DISTANCE = 27

pygame.init()
pygame.mixer.music.load('back_music.wav')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg = pygame.image.load("space_bg.png")
bg_scale = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("UFO.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("spaceship2.png")
playerimg_scale = pygame.transform.scale(playerimg,(75,75))
playerX = PLAYER_START_X
playerY =  PLAYER_START_Y
playerX_change = 0 

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6 

for i in range(number_of_enemies):
    enemyimg_new =  pygame.image.load('alien_spaceship.png')
    enemyimg_scale = pygame.transform.scale(enemyimg_new,(50,50))
    enemyimg.append(enemyimg_scale) 
    enemyX.append(random.randint(0,SCREEN_WIDTH - 64 )) 
    enemyY.append(random.randint(ENEMY_START_Y_MIN , ENEMY_START_Y_MAX)) 
    enemyX_change.append(ENEMY_SPEED_X) 
    enemyY_change.append(ENEMY_SPEED_Y) 

bulletimg = pygame.image.load("fire_bullet.png")
bulletimg_scale = pygame.transform.scale(bulletimg,(30,30))
bulletX = 0 
bulletY = PLAYER_START_Y
bulletX_change = 0 
bulletY_change = BULLET_SPEED_Y 
bullet_state = "ready"

score_value = 0 
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
over_font =  pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score,(x,y))

def game_over_text():
    pygame.mixer.music.pause()
    over_text = over_font.render("GAME OVER!!!",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerimg_scale,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg_scale,(x+16,y+10)) 

def iscollision(enemyX ,enemyY,bulletX ,bulletY):
    distance = math.sqrt((enemyX  - bulletX )**2+(enemyY - bulletY)**2)
    return distance < COLLSION_DISTANCE  

running = True 
while running:
    screen.fill((0,0,0))
    screen.blit(bg_scale,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                playerX_change = -5    
            if event.key == pygame.K_RIGHT: 
                playerX_change = +5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX =  playerX        
                fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0 
    playerX += playerX_change 
    playerX = max(0,min(playerX,SCREEN_WIDTH - 64))

    for i in range(number_of_enemies):
        if enemyY[i]> 625:
                        

            game_over_text()
            break 
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64 :
            enemyX_change[i] *= -1 
            enemyY[i] += enemyY_change[i]

        if iscollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY = PLAYER_START_Y   
            bullet_state = "ready"
            score_value += 1 
            enemyX[i] = random.randint(0,SCREEN_WIDTH - 64 )
            enemyY[i] = random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)

        enemy(enemyX[i],enemyY[i],i)

    if bulletY <= 0 :
        bulletY = PLAYER_START_Y  
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    player(playerX,playerY)
    show_score(textX,textY) 

    pygame.display.update()   