import pygame

class Bird:
    def __init__(self, screenWidth, screenHeight) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        
        self.gravity = 0.5
        self.jumpPower = -9.0
        self.velY = 0.0
        self.angle = 0
        self.x = self.screenWidth//5
        self.y = self.screenHeight//4

        self.origImg = pygame.image.load("assets/bird.png").convert_alpha()
        self.origImg = pygame.transform.smoothscale(self.origImg, (60, 38))
        self.image = self.origImg.copy()
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.hitbox = self.rect.inflate(-20, 0)
        self.hitbox.center = self.rect.center

    def draw (self, screen):
        screen.blit(self.image, self.rect)

    def update (self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    self.velY = self.jumpPower

        self.velY += self.gravity
        self.rect.y += self.velY
        # moving up velY is -ive
        # so vice versa is down
        self.angle = -self.velY
        self.image = pygame.transform.rotate(self.origImg, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        self.hitbox.center = self.rect.center

    def collsion (self, other) -> bool:
        if self.hitbox.colliderect(other.rect):
            return True

        return False
    
    def resetBird (self):
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.velY = 0
        self.angle = 0
        self.image = self.origImg.copy()
        self.hitbox.center = self.rect.center
