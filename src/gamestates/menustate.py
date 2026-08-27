from src.ui.text import Text

class MenuState:
    def __init__ (self, screenWidth, screenHeight)->None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.gameName = Text("Flappy Burd", screenWidth//2, screenHeight//2)
       
    def draw (self, screen):
        self.gameName.draw(screen)


