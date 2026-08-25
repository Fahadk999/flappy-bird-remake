import pygame

class Pipe:
    def __init__(
            self,
            screenWidth,
            screenHeight,
            rotation=0
        ) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.speed = 5


        self.image = pygame.image.load("assets/pipe.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 500))
        self.rect = self.image.get_rect(center=(100,500))
        if rotation == 1:
            # For Down Faing Pipe
            self.image = pygame.transform.rotate(self.image, 180)
            # self.upMinY = -420
            # self.upMaxY = 0
        # For Up Facing Pipe
        self.upMinY = self.screenHeight-self.rect.height
        self.upMaxY = self.screenHeight-80
        self.gap = 100

        self.rect.x = self.screenWidth

        self.hitbox = self.rect.inflate(-10, 0)
        self.hitbox.center = self.rect.center

    def update (self):
        self.hitbox.center = self.rect.center
        self.rect.x -= self.speed

    def draw (self, screen):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, "blue", self.rect, width=2)
