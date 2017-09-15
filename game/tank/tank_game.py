import pygame,sys

class Tank_game:
    def __init__(self, width=680, height=460):
        self.width = width
        self.height = height

        pygame.init()

        self.screan = pygame.display.set_mode( [self.width, self.height] )
        self.screan.fill([255,255,255])
        pygame.display.flip()



        pygame.time.delay(2)
        self.tank = pygame.image.load("player1.gif")
        self.screan.blit(self.tank, [150,100])
        pygame.display.flip()

        self.listenEvent()


    def listenEvent(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()








tankGame = Tank_game()
