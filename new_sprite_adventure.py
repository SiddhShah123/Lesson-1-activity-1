import pygame 

def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Sqaure Sprite Color Game')

    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }

    current_color = colors['white']
    x, y = 30, 30
    SPRITE_WIDTH, SPRITE_HEIGHT = 100, 100
    clock = pygame.time.Clock()
    done = False 

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3        

        x = min(max(0, x), SCREEN_WIDTH - SPRITE_WIDTH)
        y = min(max(0, y), SCREEN_HEIGHT - SPRITE_HEIGHT)

        if x == 0: 
            current_color = colors['blue']
        elif x == SCREEN_WIDTH - SPRITE_WIDTH: 
            current_color = colors['yellow']
        elif y == 0: 
            current_color = colors['red']
        elif y == SCREEN_HEIGHT - SPRITE_HEIGHT: 
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == '__main__':
    main()
