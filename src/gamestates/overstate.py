from src.ui.text import Text

class OverState:
    def __init__(self, screenWidth, screenHeight) -> None:
        # over title , retry option, and score display
        self.overTxt = Text("GAE", screenWidth//2, screenHeight//2)

    def draw (self, screen):
        self.overTxt.draw(screen)

    