import os

import pygame, sys, time
from os import path

class My_ball(pygame.sprite.Sprite):
    def __init__(self, file, locate, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = locate
        self.speed = speed

    def move(self, speed):
        self.rect = self.rect.move(speed)

class Game_class:
    def __init__(self):
        self.myBall = My_ball("beach_ball.png", [100,100], [30,0])
        size = width,height = 640, 480

        pygame.init()
        screan = pygame.display.set_mode(size)
        screan.fill([255,255,255])
        screan.blit(self.myBall.image, self.myBall.rect)

        self.screan = screan
        pygame.display.flip();

        self.clock = pygame.time.Clock()

        self.listenEvent()
    def listenEvent(self):

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        direction = 1

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.USEREVENT:

                    self.myBall.move([direction*self.myBall.speed[0], 0])
                    if self.myBall.rect.left <= 0 or self.myBall.rect.left >= self.screan.get_rect().right:
                        direction = -direction

            self.clock.tick(30)
            self.screan.fill([255,255,255])
            self.screan.blit(self.myBall.image, self.myBall.rect)

            fontObj = pygame.font.Font(os.path.join('fonts','simsun.ttc'), 50)
            fontSuface = fontObj.render((u"Game Start (游戏开始)!"),1,[255,0,0])
            self.screan.blit(fontSuface, [(self.screan.get_width()-fontSuface.get_width())/2,100])

            pygame.display.flip()

game = Game_class()