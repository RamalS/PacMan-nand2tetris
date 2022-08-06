import pygame
from bitstring import Bits

pygame.init()

line_color = (66, 135, 245)
rect_color = (0, 0, 0)

screen_size = [500, 500]
dimensions = [16, 16]

screen = pygame.display.set_mode(screen_size)
grid = [[0 for x in range(dimensions[0])] for y in range(dimensions[1])]

running = True

def collision(x, y, dimension, i, j):
    if (x >= i and x <= i + dimension and y >= j and y <= j + dimension):
        return True
    return False

def writeToFile(grid):
    i = 0
    with open('sprite.txt', 'w') as f:
        for g in grid:
            bina = "".join([str(x) for x in g])[::-1]
            a = Bits(bin=bina)
            to_write = f" let sprite[{i}] = {a.int};\n"
            #to_write = f"do Memory.poke(location + {i*32}, {a.int});\n"
            f.write(to_write)
            i += 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))

    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for i in range(1, dimensions[0]):
        step = screen_size[0] / dimensions[0] * i
        pygame.draw.line(screen, line_color, (step, 0), (step, screen_size[1]))

    for i in range(1, dimensions[1]):
        step = screen_size[1] / dimensions[1] * i
        pygame.draw.line(screen, line_color, (0, step), (screen_size[0], step))

    ev = pygame.event.get()
    left, middle, right = pygame.mouse.get_pressed()
    if (left):
        #print("pritisnuto")
        pos = pygame.mouse.get_pos()
        for i in range(0, dimensions[0]):
            for j in range(0, dimensions[1]):
                wh = 500/16
                if (collision(pos[0], pos[1], wh, int(wh * j), int(wh * i))):
                    if (grid[i][j] == 0):
                        print("colided")
                        grid[i][j] = 1

        print("----------------------")
        for i in grid:
            for j in i:
                print(j, end=" ")
            print()
        print("----------------------")
    elif (right):
        pos = pygame.mouse.get_pos()
        for i in range(0, dimensions[0]):
            for j in range(0, dimensions[1]):
                wh = 500/16
                if (collision(pos[0], pos[1], wh, int(wh * j), int(wh * i))):
                    if (grid[i][j] == 1):
                        print("colided")
                        grid[i][j] = 0

        print("----------------------")
        for i in grid:
            for j in i:
                print(j, end=" ")
            print()
        print("----------------------")
    elif (middle):
        writeToFile(grid)
        pygame.time.wait(1000)
            
    for i in range(0, dimensions[0]):
        for j in range(0, dimensions[1]):
            if (grid[i][j] == 1):
                stepx = screen_size[0] / dimensions[0] * j
                stepy = screen_size[1] / dimensions[1] * i
                w = screen_size[0] / dimensions[0]
                h = screen_size[1] / dimensions[1]
                pygame.draw.rect(screen, rect_color, pygame.Rect(stepx, stepy, w, h))

    pygame.display.flip()

pygame.quit()