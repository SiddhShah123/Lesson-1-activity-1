import pygame 
pygame.init()
screen = pygame.display.set_mode((750,750))
screen.fill((255,255,255))
GREEN = (0,255,0)
pygame.draw.circle(screen,GREEN,(300,300),50)
pygame.draw.circle(screen,GREEN,(200,200),50,3)
pygame.display.update()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()