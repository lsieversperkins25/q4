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
            
M = 20
N = 24 
num_bombs = 99 
mega_list = [] 
for m in range(M):
    mega_list.append([])
    for n in range(N):
        mega_list[m].append(0)
bombs = 1
while bombs < 100:
    row = random.randint(0,M)
    col = random.randint(0,N) 
    if mega_list[row][col] >= 0: 
        mega_list[row][col] = -1 
        bombs += 1

for rows in (0,20):
    for columns in (0,24):
        if mega_list[rows][columns] != -1:
            if rows == 0 and columns == 0:
                if mega_list[0][1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[1][0] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[1][1] == -1:
                    mega_list[rows][columns] += 1
            while columns == 0 and 1 <= rows and rows <= 18:
                if mega_list[rows-1][columns] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns] == -1:
                    mega_list[rows][columns] += 1
            if rows == 19 and columns == 0:
                if mega_list[18][0] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[18][1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[19][1] == -1:
                    mega_list[rows][columns] += 1
            while rows == 19 and 1 <= columns and columns <= 22:
                if mega_list[rows][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows][columns+1] == -1:
                    mega_list[rows][columns] += 1
            if rows == 19 and columns == 23:
                if mega_list[19][22] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[18][22] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[13][23] == -1:
                    mega_list[rows][columns] += 1
            while columns == 23 and 1 <= rows and rows <= 18:
                if mega_list[rows-1][columns] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns] == -1:
                    mega_list[rows][columns] += 1
            if rows == 0 and columns == 23:
                if mega_list[1][23] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[1][22] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[0][22] == -1:
                    mega_list[rows][columns] += 1
            while rows == 0 and 1 <= columns and columns <= 22:
                if mega_list[rows][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows][columns+1] == -1:
                    mega_list[rows][columns] += 1
            while 1 <= rows and rows <= 18 and 1 <= columns and columns <= 23:
                if mega_list[rows][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows-1][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows][columns+1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns-1] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns] == -1:
                    mega_list[rows][columns] += 1
                if mega_list[rows+1][columns+1] == -1:
                    mega_list[rows][columns] += 1


                    






        
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
