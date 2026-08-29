import pygame
from src.ui.text import Text
from src.ui.imageloader import LoadImage
from src.soundloader import LoadSound
from abs_path import absPath

class MenuState:
    def __init__ (self, screenWidth, screenHeight)->None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        titlePath = absPath("assets/flappyburd.png")
        playPath = absPath("assets/play.png")
        buttonSfxPath = absPath("assets/sounds/buttonclick.wav")

        self.titleImg = LoadImage(titlePath, 1, screenWidth//2, screenHeight//2)
        self.playImg = LoadImage(playPath, 1, screenWidth//2, screenHeight-screenHeight//3)
        self.buttonSound = LoadSound(buttonSfxPath, 0.5)
       
    def draw (self, screen):
        self.titleImg.draw(screen)
        self.playImg.draw(screen)

    def update (self, events, currState, dt):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.buttonSound.play()
                    currState = "PLAY"
        self.titleImg.idleAnimationY(dt, 2, 100)

        return currState
                    



