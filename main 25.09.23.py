import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
background.fill(pygame.Color("#FFFFFF"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw the background image on the screen
    screen.blit(background, (0, 0))

    pygame.display.flip()
pygame.quit()
