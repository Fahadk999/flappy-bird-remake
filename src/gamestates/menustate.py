import pygame
from src.ui.text import Text

class MenuState:
    def __init__ (self, screenWidth, screenHeight)->None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.gameName = Text("Flappy Burd", screenWidth//2, screenHeight//2)
       
    def draw (self, screen):
        self.gameName.draw(screen)

    def update (self, events, currState):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    currState = "PLAY"

        return currState
                    



