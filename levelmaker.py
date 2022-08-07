import pygame
from bitstring import Bits

pygame.init()

line_color = (66, 135, 245)
rect_color = (0, 0, 0)

screen_size = [1000, 500]
dimensions = [32, 16]

screen = pygame.display.set_mode(screen_size)
grid = [[0 for x in range(dimensions[0])] for y in range(dimensions[1])]

running = True

upimg = pygame.image.load('./assets/up.png')
donwimg = pygame.image.load('./assets/down.png')
leftimg = pygame.image.load('./assets/left.png')
rightimg = pygame.image.load('./assets/right.png')
verticalimg = pygame.image.load('./assets/vertical.png')
horisontalimg = pygame.image.load('./assets/horizontal.png')
tlimg = pygame.image.load('./assets/tl.png')
trimg = pygame.image.load('./assets/tr.png')
blimg = pygame.image.load('./assets/bl.png')
brimg = pygame.image.load('./assets/br.png')
dotimg = pygame.image.load('./assets/dot.png')
abilityimg = pygame.image.load('./assets/ability.png')
teleportimg = pygame.image.load('./assets/teleport.png')
htimg = pygame.image.load('./assets/ht.png')
hbimg = pygame.image.load('./assets/hb.png')
vrimg = pygame.image.load('./assets/vr.png')
vlimg = pygame.image.load('./assets/vl.png')
ghostleftimg = pygame.image.load('./assets/ghostleft.png')
ghostrightimg = pygame.image.load('./assets/ghostright.png')
pacmanimg = pygame.image.load('./assets/pacman.png')

upimg = pygame.transform.scale(upimg, (500/16, 500/16))
leftimg = pygame.transform.scale(leftimg, (500/16, 500/16))
rightimg = pygame.transform.scale(rightimg, (500/16, 500/16))
donwimg = pygame.transform.scale(donwimg, (500/16, 500/16))
verticalimg = pygame.transform.scale(verticalimg, (500/16, 500/16))
horisontalimg = pygame.transform.scale(horisontalimg, (500/16, 500/16))
tlimg = pygame.transform.scale(tlimg, (500/16, 500/16))
trimg = pygame.transform.scale(trimg, (500/16, 500/16))
blimg = pygame.transform.scale(blimg, (500/16, 500/16))
brimg = pygame.transform.scale(brimg, (500/16, 500/16))
dotimg = pygame.transform.scale(dotimg, (500/16, 500/16))
abilityimg = pygame.transform.scale(abilityimg, (500/16, 500/16))
teleportimg = pygame.transform.scale(teleportimg, (500/16, 500/16))
htimg = pygame.transform.scale(htimg, (500/16, 500/16))
hbimg = pygame.transform.scale(hbimg, (500/16, 500/16))
vrimg = pygame.transform.scale(vrimg, (500/16, 500/16))
vlimg = pygame.transform.scale(vlimg, (500/16, 500/16))
ghostleftimg = pygame.transform.scale(ghostleftimg, (500/16, 500/16))
ghostrightimg = pygame.transform.scale(ghostrightimg, (500/16, 500/16))
pacmanimg = pygame.transform.scale(pacmanimg, (500/16, 500/16))

print(len(grid[0]))

ar = 500/16

def collision(x, y, dimension, i, j):
    if (x >= i and x <= i + dimension and y >= j and y <= j + dimension):
        return True
    return False

def writeToFile(grid):
    i = 0
    with open('map.txt', 'w') as f:
        for g in grid:
            for it in g:
                to_write = f" let map[{i}] = {it};\n"
                f.write(to_write)
                i += 1

def load():
    i = 0
    j = 0
    map_name = input("map name: ")
    with open(f'./saves/{map_name}.txt') as f:
        for line in f:
            if j > 31:
                i += 1
                j = 0
            grid[i][j] = int(line)
            j += 1
def save():
    map_name = input("map name: ")
    with open(f'./saves/{map_name}.txt', 'w') as f:
        for g in grid:
            for it in g:
                to_write = f"{it}\n"
                f.write(to_write)

block = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_1):
                block = 7
                print("up")
            elif (event.key == pygame.K_2):
                block = 8
                print("down")
            elif (event.key == pygame.K_3):
                block = 9
                print("left")
            elif (event.key == pygame.K_4):
                block = 10
                print("right")
            elif (event.key == pygame.K_5):
                block = 11
                print("vertical")
            elif (event.key == pygame.K_6):
                block = 12
                print("horizontal")
            elif (event.key == pygame.K_7):
                block = 13
                print("top left")
            elif (event.key == pygame.K_8):
                block = 14
                print("top right")
            elif (event.key == pygame.K_9):
                block = 15
                print("bottom left")
            elif (event.key == pygame.K_0):
                block = 16
                print("bottom right")
            elif (event.key == pygame.K_UP):
                block = 17
                print("horizontal top")
            elif (event.key == pygame.K_DOWN):
                block = 18
                print("horizontal bottom")
            elif (event.key == pygame.K_RIGHT):
                block = 19
                print("vertical right")
            elif (event.key == pygame.K_LEFT):
                block = 20
                print("vertical left")
            elif (event.key == pygame.K_d):
                block = 1
                print("dot")
            elif (event.key == pygame.K_a):
                block = 2
                print("ability")
            elif (event.key == pygame.K_t):
                block = 3
                print("teleport")
            elif (event.key == pygame.K_p):
                block = 4
                print("pacman")
            elif (event.key == pygame.K_j):
                block = 5
                print("ghost left")
            elif (event.key == pygame.K_k):
                block = 6
                print("ghost right")
            elif (event.key == pygame.K_l):
                load()
            elif (event.key == pygame.K_s):
                save()
            


    screen.fill((255, 255, 255))

    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for i in range(1, dimensions[0]):
        step = ar * i
        pygame.draw.line(screen, line_color, (step, 0), (step, screen_size[1]))

    for i in range(1, dimensions[1]):
        step = ar * i
        pygame.draw.line(screen, line_color, (0, step), (screen_size[0], step))

    ev = pygame.event.get()
    left, middle, right = pygame.mouse.get_pressed()
    if (left):
        #print("pritisnuto")
        pos = pygame.mouse.get_pos()
        for i in range(0, 16):
            for j in range(0, 32):

                if (collision(pos[0], pos[1], ar, int(ar * j), int(ar * i))):
                    if (grid[i][j] == 0):
                        #print("colided")
                        grid[i][j] = block

        # print("----------------------")
        # for i in grid:
        #     for j in i:
        #         print(j, end=" ")
        #     print()
        # print("----------------------")
    elif (right):
        pos = pygame.mouse.get_pos()
        for i in range(0, 16):
            for j in range(0, 32):
                if (collision(pos[0], pos[1], ar, int(ar * j), int(ar * i))):
                    if (grid[i][j] > 0):
                        #print("colided")
                        grid[i][j] = 0

        # print("----------------------")
        # for i in grid:
        #     for j in i:
        #         print(j, end=" ")
        #     print()
        # print("----------------------")
    elif (middle):
        writeToFile(grid)
        pygame.time.wait(1000)
            
    for i in range(0, 16):
        for j in range(0, 32):
            if (grid[i][j] > 0):
                stepx = ar * j
                stepy = ar * i

                blo = grid[i][j]

                if (blo == 7):
                    screen.blit(upimg, (stepx, stepy))
                elif (blo == 8):
                    screen.blit(donwimg, (stepx, stepy))
                elif (blo == 9):
                    screen.blit(leftimg, (stepx, stepy))
                elif (blo == 10):
                    screen.blit(rightimg, (stepx, stepy))
                elif (blo == 11):
                    screen.blit(verticalimg, (stepx, stepy))
                elif (blo == 12):
                    screen.blit(horisontalimg, (stepx, stepy))
                elif (blo == 13):
                    screen.blit(tlimg, (stepx, stepy))
                elif (blo == 14):
                    screen.blit(trimg, (stepx, stepy))
                elif (blo == 15):
                    screen.blit(blimg, (stepx, stepy))
                elif (blo == 16):
                    screen.blit(brimg, (stepx, stepy))
                elif (blo == 17):
                    screen.blit(htimg, (stepx, stepy))
                elif (blo == 18):
                    screen.blit(hbimg, (stepx, stepy))
                elif (blo == 19):
                    screen.blit(vrimg, (stepx, stepy))
                elif (blo == 20):
                    screen.blit(vlimg, (stepx, stepy))
                elif (blo == 1):
                    screen.blit(dotimg, (stepx, stepy))
                elif (blo == 2):
                    screen.blit(abilityimg, (stepx, stepy))
                elif (blo == 3):
                    screen.blit(teleportimg, (stepx, stepy))
                elif (blo == 4):
                    screen.blit(pacmanimg, (stepx, stepy))
                elif (blo == 5):
                    screen.blit(ghostleftimg, (stepx, stepy))
                elif (blo == 6):
                    screen.blit(ghostrightimg, (stepx, stepy))

    pygame.display.flip()

pygame.quit()