import pygame

class Pipe:
    def __init__(self, screenWidth, screenHeight, rotation=0) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.speed = 5

        # For Up-Pipe
        self.upMinY = 0
        self.upMaxY = self.screenHeight-60

        self.image = pygame.image.load("assets/pipe.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 500))
        if rotation == 1:
            self.image = pygame.transform.rotate(self.image, 180)
            self.upMinY = -420
            self.upMaxY = 0

        self.rect = self.image.get_rect(center=(100,500))
        self.hitbox = self.rect.inflate(-10, 0)
        self.hitbox.center = self.rect.center
        self.rect.y = self.upMinY

    def update (self):
        self.hitbox.center = self.rect.center

    def draw (self, screen):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, "blue", self.rect, width=2)
    def newY (self, pos):
        self.rect.y = pos
