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
                block = 3
                print("up")
            elif (event.key == pygame.K_2):
                block = 4
                print("down")
            elif (event.key == pygame.K_3):
                block = 5
                print("left")
            elif (event.key == pygame.K_4):
                block = 6
                print("right")
            elif (event.key == pygame.K_5):
                block = 7
                print("vertical")
            elif (event.key == pygame.K_6):
                block = 8
                print("horizontal")
            elif (event.key == pygame.K_7):
                block = 9
                print("top left")
            elif (event.key == pygame.K_8):
                block = 10
                print("top right")
            elif (event.key == pygame.K_9):
                block = 11
                print("bottom left")
            elif (event.key == pygame.K_0):
                block = 12
                print("bottom right")
            elif (event.key == pygame.K_d):
                block = 1
                print("dot")
            elif (event.key == pygame.K_a):
                block = 2
                print("ability")
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

                if (blo == 3):
                    screen.blit(upimg, (stepx, stepy))
                elif (blo == 4):
                    screen.blit(donwimg, (stepx, stepy))
                elif (blo == 5):
                    screen.blit(leftimg, (stepx, stepy))
                elif (blo == 6):
                    screen.blit(rightimg, (stepx, stepy))
                elif (blo == 7):
                    screen.blit(verticalimg, (stepx, stepy))
                elif (blo == 8):
                    screen.blit(horisontalimg, (stepx, stepy))
                elif (blo == 9):
                    screen.blit(tlimg, (stepx, stepy))
                elif (blo == 10):
                    screen.blit(trimg, (stepx, stepy))
                elif (blo == 11):
                    screen.blit(blimg, (stepx, stepy))
                elif (blo == 12):
                    screen.blit(brimg, (stepx, stepy))
                elif (blo == 1):
                    screen.blit(dotimg, (stepx, stepy))
                elif (blo == 2):
                    screen.blit(abilityimg, (stepx, stepy))

    pygame.display.flip()

pygame.quit()