import sys, pygame
red, green, blue = 0,0,0

def background_changer():
    background = input("Please enter three values between 0 and 255, comma-separated: ").split(",")
    global red, green, blue;
    red, green, blue = int(background[0]), int(background[1]), int(background[2])

    pygame.init()

    size = (800, 600)
    screen = pygame.display.set_mode(size)
    screen.fill((red, green, blue))
    pygame.display.update()

    color_rotation = {"red":"green", "green":"blue", "blue":"red"}
    current_color = "red"

    def tweak_background(amount):
        global red, green, blue
        if current_color == "red":
            red += amount
            if red > 255: red = 255
            elif red < 0: red = 0
        elif current_color == "green":
            green += amount
            if green > 255: green = 255
            elif green < 0: green = 0
        elif current_color == "blue":
            blue += amount
            if blue > 255: blue = 255
            elif blue < 0: blue = 0
        screen.fill((red, green, blue))
        pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tweak_background(10)

                elif event.key == pygame.K_DOWN:
                    tweak_background(-10)

                elif event.key == pygame.K_RIGHT:
                    current_color = color_rotation[str(current_color)]

                elif event.key == pygame.K_LEFT:
                    current_color = color_rotation[color_rotation[str(current_color)]]


