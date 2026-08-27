from src.ui.text import Text
from src.ui.imageloader import LoadImage

class OverState:
    def __init__(self, screenWidth, screenHeight) -> None:
        # over title , retry option, and score display
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.overDisplay = LoadImage("assets/gameover.png", 1, self.screenWidth//2, self.screenHeight//2)


    def draw (self, screen):
        self.overDisplay.draw(screen)

    
