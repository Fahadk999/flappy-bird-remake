import pygame
from src.ui.text import Text
from src.ui.imageloader import LoadImage

class OverState:
    def __init__(self, screenWidth, screenHeight, score=0) -> None:
        # over title , retry option, and score display
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.score = score
        self.overDisplay = LoadImage("assets/gameover.png", 1, self.screenWidth//2, self.screenHeight//2)
        self.scoreTxt = Text(f"Score: {self.score}", self.screenWidth//2, self.screenHeight-self.screenHeight//3)
        self.retryTxt = Text("Press R to Retry", self.screenWidth//2, self.screenHeight-self.screenHeight//4)

    def draw (self, screen):
        self.overDisplay.draw(screen)
        self.scoreTxt.draw(screen)
        self.retryTxt.draw(screen)

    def updateScore (self, newScore):
        self.score = newScore
        self.scoreTxt.updateText(f"Score: {int(self.score)}")

