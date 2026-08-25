from src.bird import Bird
from src.pipe import Pipe

class PlayState:
    def __init__(self, screenWidth, screenHeight) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.bird = Bird(screenWidth, screenHeight)
        self.pipes = []

        self.pipeSpawnTimer = 0
        self.pipeSpawnInterval = 1500

    def update (self, events, dt):
        self.bird.update(events)
        self.spawnPipe(dt)
        for p in self.pipes:
            p.update()

    def draw (self, screen):
        self.bird.draw(screen)
        for p in self.pipes:
            p.draw(screen)

    def spawnPipe (self, dt):
        # every 1.5 seconds
        self.pipeSpawnTimer += dt

        if self.pipeSpawnTimer >= self.pipeSpawnInterval:
            self.pipes.append(Pipe(self.screenWidth, self.screenHeight))
            self.pipeSpawnTimer -= self.pipeSpawnInterval
        
