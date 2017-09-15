import random, time, pygame, math
from pygame.color import THECOLORS

import sys


def createRandom():
    resultList = []
    for i in range(5):
        resultList.append(random.randint(1,20))
    return  resultList

def printTimer():
    for i in range(30):

        time.sleep(1)
        if( (i+1) % 3 == 0):
            print(random.random())

def drawRect(screen):
    for i in range(100):
        left = random.randint(0, 255)
        top = random.randint(0, 100)
        width = random.randint(0,400)
        height = random.randint(0,500)
        border = random.randint(1,5)
        pygame.draw.rect(screen, [left,top,0], [left, top, width, height], border)

def drawWaveLine(screen):
    #
    for x in range(0, 640):
        y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240 )
        pygame.draw.rect(screen, [255,0,0], [x,y,1,1], 2)

def drawLine(screen):
    #绘制曲线
    points = []
    for x in range(0, 640):
        y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)
        points.append([x,y])

    pygame.draw.lines(screen, [255,0,0], False, points, 2)


def drawLeaves(screen):
    #绘制树叶
    points = dots = [[221, 432], [225, 331], [133, 342], [141, 310], [51, 230], [74, 217], [58, 153], [114, 164],
                     [123, 135], [176, 190], [159, 77], [193, 93], [230, 28], [267, 93], [301, 77], [284, 190],
                     [327, 135], [336, 164], [402, 153], [386, 217], [409, 230], [319, 310], [327, 342], [233, 331],
                     [237, 432]]
    pygame.draw.lines(screen, [255,0,0], True, points, 2)

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0], [100,100],50, 1)

# drawRect(screen)
# drawWaveLine(screen)
drawLeaves(screen)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
