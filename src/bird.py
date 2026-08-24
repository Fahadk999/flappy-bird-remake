import pygame

class Bird:
    def __init__(self, screenWidth, screenHeight) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.gravity = 0.5
        self.jumpPower = -18.0
        self.velY = 0.0
        self.image = pygame.image.load("assets/bird.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (102, 64))
        self.rect = self.image.get_rect(center=(100,300))
        self.hitbox = self.rect.inflate(-30, 0)
        self.hitbox.center = self.rect.center
        self.rect.topleft = (
            self.screenWidth//5,
            self.screenHeight//2 - self.rect.height//2
        )

    def draw (self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, "blue", self.rect, width=2)
        pygame.draw.rect(screen, "red", self.hitbox, width=2)

    def update (self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    self.velY = self.jumpPower

        self.velY += self.gravity
        self.rect.y += self.velY
        self.hitbox.center = self.rect.center
