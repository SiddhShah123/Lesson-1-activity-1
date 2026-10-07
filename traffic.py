
import pygame, random

CHANGE_SIGNAL = pygame.USEREVENT + 1 

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=(100, 100))
        self.vx, self.vy = 4, 3

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left <= 0 or self.rect.right >= 600:
            self.vx *= -1
            pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.vy *= -1
            pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))

    def change_color(self):
        self.image.fill((random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

car = Car()
sprites = pygame.sprite.Group(car)
signal_color = 'green'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_SIGNAL:
            signal_color = 'red' if signal_color == 'green' else 'green'
            car.change_color()

    sprites.update()
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, signal_color, (550, 40), 20) 
    sprites.draw(screen)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

