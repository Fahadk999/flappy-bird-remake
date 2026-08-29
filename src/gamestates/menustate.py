import pygame
from src.ui.text import Text
from src.ui.imageloader import LoadImage

class MenuState:
    def __init__ (self, screenWidth, screenHeight)->None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        titlePath = "assets/flappyburd.png"
        playPath = "assets/play.png"

        self.titleImg = LoadImage(titlePath, 1, screenWidth//2, screenHeight//2)
        self.playImg = LoadImage(playPath, 1, screenWidth//2, screenHeight-screenHeight//3)
       
    def draw (self, screen):
        self.titleImg.draw(screen)
        self.playImg.draw(screen)

    def update (self, events, currState, dt):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    currState = "PLAY"
        self.titleImg.idleAnimationY(dt, 2, 100)

        return currState
                    



