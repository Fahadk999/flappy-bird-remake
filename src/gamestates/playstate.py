from src.bird import Bird
from src.pipe import Pipe

class PlayState:
    def __init__(self, screenWidth, screenHeight) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.bird = Bird(screenWidth, screenHeight)
        self.pipe = Pipe(screenWidth, screenHeight)
        self.otherpipe = Pipe(screenWidth, screenHeight, rotation=1)

    def update (self, events):
        self.pipe.newY(self.pipe.upMaxY)
        self.bird.update(events)

    def draw (self, screen):
        self.bird.draw(screen)
        self.pipe.draw(screen)
        self.otherpipe.draw(screen)
        