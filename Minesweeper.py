# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos() 
            
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("PaleTurquoise")
    more_rectangles = True
    row = 1
    column = 1
    color = 'green3'
    x1 = 250
    y1 = 50
    while more_rectangles == True:
        if color == 'green3':
            color = 'green2'
        else:
            color = 'green3'
        if column < 24:
            pygame.draw.rect(screen, color, [x1, y1, 30, 30])
            column += 1
            x1 += 30
        elif column == 24:
            pygame.draw.rect(screen, color, [x1, y1, 30, 30])
            column = 1
            y1 += 30
            x1 = 250
            row += 1
            if color == 'green3':
                color = 'green2'
            else:
                color = 'green3'
            if row == 21:
                more_rectangles = False
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
