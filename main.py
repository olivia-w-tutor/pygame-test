import sys, pygame
pygame.init()

size = (800, 600)
background = (100, 0, 0)
screen = pygame.display.set_mode(size)
screen.fill(background)
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                background = (background[0] + 10, 0, 0)
                screen.fill(background)
                pygame.display.update()
            elif event.key == pygame.K_DOWN:
                background = (background[0]-10, 0, 0)
                screen.fill(background)
                pygame.display.update()


pygame.quit()

