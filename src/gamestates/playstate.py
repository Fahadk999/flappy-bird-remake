from src.ui.text import Text
from random import randint
from src.bird import Bird
from src.pipe import Pipe

class PlayState:
    def __init__(self, screenWidth, screenHeight) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.bird = Bird(screenWidth, screenHeight)
        self.pipes = []
        self.score = 0
        self.scoreStr = f"Score: {int(self.score)}"
        self.scoreTxt = Text(self.scoreStr, 75, 25)

        self.pipeGap = 200
        self.pipeSpawnTimer = 0
        self.pipeSpawnInterval = 1500

    def update (self, events, dt, currState):
        self.score += dt/1000
        self.bird.update(events)
        self.spawnPipe(dt)
        for p in self.pipes:
            p.update()
            if self.bird.collsion(p):
               currState = "OVER"
        if self.bird.rect.y > self.screenHeight+200:
           currState = "OVER"
        elif self.bird.rect.y < -200:
           currState = "OVER"

        self.scoreTxt.updateText(f"Score: {int(self.score)}")
        return currState

    def draw (self, screen):
        self.bird.draw(screen)
        for p in self.pipes:
            p.draw(screen)

        self.scoreTxt.draw(screen)

    def spawnPipe (self, dt):
        # every 1.5 seconds
        self.pipeSpawnTimer += dt

        if self.pipeSpawnTimer >= self.pipeSpawnInterval:
            upPipe = Pipe(self.screenWidth, self.screenHeight)
            downPipe = Pipe(self.screenWidth, self.screenHeight, rotation=1)
            pipeHeight = upPipe.rect.height
            posY = randint(upPipe.upMinY, upPipe.upMaxY) # will be rand, limits will be the max and min Y of the up pipe
            upPipe.setPosY(posY)
            downPipe.setPosY(upPipe.rect.y-pipeHeight-self.pipeGap)
            self.pipes.append(upPipe)
            self.pipes.append(downPipe)
            self.pipeSpawnTimer -= self.pipeSpawnInterval

    def resetGame (self):
        self.pipes.clear()
        self.score = 0
        self.scoreStr = f"Score: {int(self.score)}"
        self.scoreTxt = Text(self.scoreStr, 75, 25)
        self.pipeSpawnTimer = 0
        self.bird.resetBird()
        
