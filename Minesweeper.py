# Example file showing a basic pygame "game loop"
import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screen.fill('PaleTurquoise')
more_rectangles = True
row = 1
column = 1
color = 'green3'
x1 = 250
y1 = 50
list_of_rectangles = []
while more_rectangles == True:
    if color == 'green3':
        color = 'green2'
    else:
        color = 'green3'
    if column < 24:
        list_of_rectangles.append( pygame.draw.rect(screen, color, [x1, y1, 30, 30]) )
        column += 1
        x1 += 30
    elif column == 24:
        list_of_rectangles.append( pygame.draw.rect(screen, color, [x1, y1, 30, 30]) )
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
replicate_list = [thing for thing in list_of_rectangles]
bombs = 1
list_bombs = []
while bombs < 100:
    explosive = random.randint(0, 479)
    if explosive not in list_bombs:
        list_bombs.append(explosive)
        bombs+=1
for values in replicate_list:
    values = 0
for stuff in list_bombs:
    replicate_list[stuff] = -1



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            
            

    
                
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
