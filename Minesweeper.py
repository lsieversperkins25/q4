# Example file showing a basic pygame "game loop"
import random
import pygame
import math

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
x1 = 450
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
        x1 = 450
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
                    if not(r == 0 and c == 0):
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
    if double_list[q][1] != -1:
        double_list[q].append(True)
    elif double_list[q][1] == -1:
        double_list[q].append(False)
    double_list[q].append(False)
    double_list[q].append(True)

instruction_font = pygame.font.SysFont('Arial', 35)
instruction = instruction_font.render('Switch between modes', False, 'black')
instruction1 = instruction_font.render('using the space bar', False, 'black')
screen.blit(instruction, (50, 50))
screen.blit(instruction1, (75, 90))

bomb = pygame.image.load('bomb-pixel-art.png')
change_bomb = pygame.transform.scale(bomb, (30, 30))
font = pygame.font.SysFont('Arial', 200, bold = True)
one = pygame.image.load('one.png')
one = pygame.transform.scale(one, (30, 30))
two = pygame.image.load('two.png')
two = pygame.transform.scale(two, (30, 30))
three = pygame.image.load('three.png')
three = pygame.transform.scale(three, (30, 30))
four = pygame.image.load('four.png')
four = pygame.transform.scale(four, (30, 30))
five = pygame.image.load('five.png')
five = pygame.transform.scale(five, (30, 30))
six = pygame.image.load('six.png')
six = pygame.transform.scale(six, (30, 30))
seven = pygame.image.load('seven.png')
seven = pygame.transform.scale(seven, (30, 30))
eight = pygame.image.load('eight.png')
eight = pygame.transform.scale(eight, (30, 30))
zero = pygame.image.load('zero.png')
zero = pygame.transform.scale(zero, (30, 30))
flag = pygame.image.load('flag-pixel-art.png')
flag1 = pygame.transform.scale(flag, (30, 30))
click = pygame.image.load('mouse.png')

game_over = False
game_over1 = False
game_over_for_real = False
start = 0
finish = 1
flag_on = False
all_done = 0
you_win = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if you_win == True:
        winner = font.render('You Win!', True, 'green')
        screen.blit(winner, (75, 200))
    if game_over_for_real:
        pygame.time.delay(6000)
        running = False
    if game_over1:
        pygame.time.delay(500)
        you_lose = font.render('Game Over', True, 'red')
        screen.blit(you_lose, (75, 200))
        game_over1 = False
        game_over_for_real = True 
    if game_over:
        for lose in range(start, finish):
            start += 1
            finish += 1
            if double_list[lose][1] == -1:
                pygame.time.delay(5)
                screen.blit(change_bomb, (double_list[lose][0].x, double_list[lose][0].y) )
            if lose == 479:
                game_over1 = True
                game_over = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over == False:
            if event.key == pygame.K_SPACE:
                if flag_on == False:
                    flag_on = True
                else:
                    flag_on = False
        if event.type == pygame.MOUSEBUTTONUP and game_over == False:
            mouse = pygame.mouse.get_pos()
            for check in range(480):
                if double_list[check][0].collidepoint(mouse):
                    if not flag_on and double_list[check][4]:
                        if double_list[check][1] == -1:
                            screen.blit(change_bomb, (double_list[check][0].x, double_list[check][0].y) )
                            game_over = True
                        if double_list[check][1] == 1:
                            screen.blit(one, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 2:
                            screen.blit(two, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 3:
                            screen.blit(three, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 4:
                            screen.blit(four, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 5:
                            screen.blit(five, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 6:
                            screen.blit(six, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 7:
                            screen.blit(seven, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 8:
                            screen.blit(eight, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                        if double_list[check][1] == 0:
                            screen.blit(zero, (double_list[check][0].x, double_list[check][0].y) )
                            double_list[check][2] = False
                            double_list[check][3] = True
                            # We need to loop over the board 
                            #   0 -> rectangle
                            #   1 -> Number of bombs adjacent
                            #   2 -> 
                            #   3 -> Been clicked 
                            zero_looping = True
                            check_column = check % 24
                            while(zero_looping):
                                zero_looping = False 
                                for index in range(480):
                                    if double_list[index][1] == 0 and double_list[index][3]:
                                        for i in [index-25,index-24,index-23,index-1,index+1,index+23,index+24,index+25]:
                                            i_column = i % 24
                                            if i>=0 and i<480:
                                                if abs(check_column - i_column) == 1 or abs(check_column - i_column) == 0:
                                                    if not double_list[i][3]:
                                                        zero_looping = True                                             
                                                        double_list[i][2] = False
                                                        double_list[i][3] = True  
                                                        if double_list[i][1] == 0:
                                                            screen.blit(zero, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 1:
                                                            screen.blit(one, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 2:
                                                            screen.blit(two, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 3:
                                                            screen.blit(three, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 4:
                                                            screen.blit(four, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 5:
                                                            screen.blit(five, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 6:
                                                            screen.blit(six, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 7:
                                                            screen.blit(seven, (double_list[i][0].x, double_list[i][0].y) )
                                                        if double_list[i][1] == 8:
                                                            screen.blit(eight, (double_list[i][0].x, double_list[i][0].y) )
                    elif flag_on == True:
                        if double_list[check][3] == False:
                            if double_list[check][4] == True:
                                screen.blit(flag1, (double_list[check][0].x, double_list[check][0].y) )
                                double_list[check][4] = False
                            else:
                                double_list[check][0]
                                if (math.floor(check / 24) + (check % 24)) % 2 == 0:
                                    new_color = 'green2'
                                elif (math.floor(check / 24) + (check % 24)) % 2 == 1:
                                    new_color = 'green3'
                                pygame.draw.rect(screen, new_color, [double_list[check][0].x, double_list[check][0].y, 30, 30])
                                double_list[check][4] = True
                    for a in range(480):
                        if double_list[a][2] == False:
                            all_done += 1
                    if all_done == 480:
                       you_win = True
                    elif all_done != 480:
                        all_done = 0
    if flag_on == False and game_over_for_real == False:
       pygame.draw.rect(screen, 'PaleTurquoise', [125, 140, 218, 218])
       screen.blit(click, (125, 150))
    elif flag_on == True and game_over_for_real == False:
        pygame.draw.rect(screen, 'PaleTurquoise', [125, 150, 150, 190])
        screen.blit(flag, (125, 140))
                                
                            
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
