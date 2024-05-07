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
    row = random.randint(0,M-1)
    col = random.randint(0,N-1) 
    if mega_list[row][col] >= 0: 
        mega_list[row][col] = -1 
        bombs += 1

for rows in range(20):
    for columns in range(24):
        if mega_list[rows][columns] != -1:
            total = 0
            for r in range(-1,2):
                for c in range(-1,2):
                    if not( r == 0 and c == 0):
                        if rows + r >= 0 and 19 >= rows + r and columns + c >= 0 and 23 >= columns + c:
                            if mega_list[rows +r][columns + c] == -1:
                                total += 1
            mega_list[rows][columns] = total
                        
mega_list2 = []
for a in range(20):
    for b in range(24):
        mega_list2.append(mega_list[a][b])
double_list = []

for q in range(480):
    double_list.append([])
    double_list[q].append(list_of_rectangles[q])
    double_list[q].append(mega_list2[q])
    double_list[q].append(True)

bomb = pygame.image.load('bomb-pixel-art.png')
change_bomb = pygame.transform.scale(bomb, (30, 30))
font = pygame.font.SysFont('Arial', 200, bold = True)
one = pygame.image.load('one.png')
better_one = pygame.transform.scale(one, (30, 30))
two = pygame.image.load('two.png')
better_two = pygame.transform.scale(two, (30, 30))
three = pygame.image.load('three.png')
better_three = pygame.transform.scale(three, (30, 30))
four = pygame.image.load('four.png')
better_four = pygame.transform.scale(four, (30, 30))
five = pygame.image.load('five.png')
better_five = pygame.transform.scale(five, (30, 30))
six = pygame.image.load('six.png')
better_six = pygame.transform.scale(six, (30, 30))
seven = pygame.image.load('seven.png')
better_seven = pygame.transform.scale(seven, (30, 30))
eight = pygame.image.load('eight.png')
better_eight = pygame.transform.scale(eight, (30, 30))

game_over = False
game_over1 = False
game_over2 = False
game_over3 = False
game_over4 = False
game_over_for_real = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if game_over_for_real:
        pygame.time.delay(7500)
        running = False
    if game_over4:
        pygame.time.delay(500)
        you_lose = font.render('Game Over', True, 'red')
        screen.blit(you_lose, (75, 200))
        game_over4 = False
        game_over_for_real = True
    if game_over3:
        pygame.time.delay(500)
        for lose in range(360,480):
            if double_list[lose][1] == -1:
                screen.blit(change_bomb, (double_list[lose][0].x, double_list[lose][0].y) )
        game_over3 = False
        game_over4 = True
    if game_over2:
        pygame.time.delay(500)
        for lose in range(240,360):
            if double_list[lose][1] == -1:
                screen.blit(change_bomb, (double_list[lose][0].x, double_list[lose][0].y) )
        game_over2 = False
        game_over3 = True
    if game_over1:
        pygame.time.delay(500)
        for lose in range(120,240):
            if double_list[lose][1] == -1:
                screen.blit(change_bomb, (double_list[lose][0].x, double_list[lose][0].y) )
        game_over1 = False
        game_over2 = True
    if game_over:
        pygame.time.delay(500)
        for lose in range(120):
            if double_list[lose][1] == -1:
                screen.blit(change_bomb, (double_list[lose][0].x, double_list[lose][0].y) )
        game_over = False
        game_over1 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            for check in range(480):
                if double_list[check][0].collidepoint(mouse):
                    if double_list[check][1] == -1:
                        screen.blit(change_bomb, (double_list[check][0].x, double_list[check][0].y) )
                        game_over = True
                    if double_list[check][1] == 1:
                        screen.blit(better_one, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 2:
                        screen.blit(better_two, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 3:
                        screen.blit(better_three, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 4:
                        screen.blit(better_four, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 5:
                        screen.blit(better_five, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 6:
                        screen.blit(better_six, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 7:
                        screen.blit(better_seven, (double_list[check][0].x, double_list[check][0].y) )
                    if double_list[check][1] == 8:
                        screen.blit(better_eight, (double_list[check][0].x, double_list[check][0].y) )
                        
                        
                    
# bomb png background rgb color rgb(243, 246, 255)
            
            

    
                
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
