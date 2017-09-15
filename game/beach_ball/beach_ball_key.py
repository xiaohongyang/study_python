#通过键盘方向键控制 球的移动
import pygame, sys

class My_ball(pygame.sprite.Sprite):
    def __init__(self, file, locate, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = locate
        self.speed = speed

    def move(self, speed):
        self.rect = self.rect.move(speed)


class Game_ball:
    def __init__(self):
        size = width,height = 640,480
        self.clock = pygame.time.Clock()

        pygame.init()
        pygame.key.set_repeat(100, 50)

        self.screan = pygame.display.set_mode(size)
        self.screan.fill([255,255,255])

        self.background = pygame.Surface(self.screan.get_size())
        self.background.fill([255,255,255])

        self.installElement()
        self.listenEvent()

    def installElement(self):
        self.myBall = My_ball("beach_ball.png", [100, 100], [15,15])
        self.screan.blit(self.myBall.image, self.myBall.rect)
        pygame.display.flip()


    def listenEvent(self):

        held_down = False;
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    held_down = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    held_down = False

                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.myBall.move([0, -self.myBall.speed[1]])
                    elif event.key == pygame.K_DOWN:
                        self.myBall.move([0, self.myBall.speed[1]])
                    elif event.key == pygame.K_LEFT:
                        self.myBall.move([-self.myBall.speed[0], 0])
                    elif event.key == pygame.K_RIGHT:
                        self.myBall.move([self.myBall.speed[0], 0])
                elif event.type == pygame.MOUSEMOTION:
                    if held_down == True:
                        #鼠标拖动
                        self.myBall.rect.center = event.pos

            self.clock.tick(30)
            self.screan.blit(self.background, [0,0])
            self.screan.blit(self.myBall.image, self.myBall.rect)
            pygame.display.flip()


game = Game_ball()