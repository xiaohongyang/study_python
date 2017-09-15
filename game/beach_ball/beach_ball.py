from random import choice

import pygame, sys

size = width, height = 640, 480
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, file, location, speed=[5,0]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        #球的移动
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 and self.speed[0]<0:
            self.speed[0] = -self.speed[0]
        if(self.rect.left > width-self.rect.width and self.speed[0]>0):
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 and self.speed[1] < 0:
            self.speed[1] = -self.speed[1]
        if self.rect.top > height-self.rect.height and self.speed[1] > 0:
            self.speed[1] = -self.speed[1]



class Game:
    def __init__(self,width=640, height=480):

        size = width,height
        self.file = "beach_ball.png"
        self.screan = pygame.display.set_mode( size )
        self.screan.fill([255,255,255])

        #定义actors
        self.actors = pygame.sprite.Group()
        self.file = "beach_ball.png"

        pygame.init()
        pygame.display.flip()
        self.clock = pygame.time.Clock()
        self.initActors()
        self.listenEvent()

    def initActors(self):

        for row in range(2):
            for column in range(2):
                location = [row*180+50, column*180+150]
                myBall = MyBallClass(self.file, location, [choice([-12,22]), choice([-12,22])])
                self.actors.add(myBall)

        for actor in self.actors:
            self.screan.blit(actor.image, actor.rect)
            pygame.display.flip()

    def animate(self):
        #运动
        if len(self.actors) > 0:
                self.screan.fill([255,255,255])
                for actor in self.actors:
                    actor.move()
                    self.screan.blit(actor.image, actor.rect)
                for actor in self.actors:
                    self.actors.remove(actor)
                    if pygame.sprite.spritecollide(actor, self.actors, False):
                        actor.speed[0] = -actor.speed[0]
                        actor.speed[1] = -actor.speed[1]
                    self.actors.add(actor)
                    print("frame_rate:", self.clock.get_fps())
                pygame.display.flip()

    def listenEvent(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.animate()
            self.clock.tick(30)




game = Game()
