import pygame

pygame.init()
size = (720,720)
screen = pygame.display.set_mode(size)

color = (255,255,255)

color_light = (170,170,170)
color_dark = (100,100,100)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)

text = smallfont.render('quit',True, color)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()

    screen.fill((60,25,60))

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2, height/2, 140, 40])

    else:
        pygame.draw.rect(screen,color_dark,[width/2, height/2, 140, 40])

    screen.blit(text, (width/2+50, height/2))

    pygame.display.update()