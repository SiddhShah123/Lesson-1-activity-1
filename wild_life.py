import pygame

# Initialize Pygame and screen dimensions.
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wild life and Facts')

# Load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load('wildlife_background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

animals_image = pygame.transform.scale(
    pygame.image.load('animals.png').convert_alpha(), (250, 250))
animals_rect = animals_image.get_rect(center=(SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2 - 30))

# Initialize font, render text, and set text position
text = pygame.font.Font(None, 20).render('Blue whales are the largest animals to have ever lived on Earth, with a heart the size of a small car. ', True,
    pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(animals_image, animals_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()