import pygame
from src.ui.text import Text
from src.ui.imageloader import LoadImage

class OverState:
    def __init__(self, screenWidth, screenHeight, score=0) -> None:
        # over title , retry option, and score display
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.score = score
        overPath = "assets/gameover.png"
        retryPath = "assets/retry.png"
        self.overImg = LoadImage(overPath, 1, self.screenWidth//2, self.screenHeight//5)
        self.scoreTxt = Text(f"Score: {self.score}", self.screenWidth//2, self.screenHeight//3)
        self.scoreList = [] 
        self.retryImg = LoadImage(retryPath, 1, self.screenWidth//2, self.screenHeight-self.screenHeight//4)
        self.topScoreTxt = Text("Top Scores", self.screenWidth//2, self.scoreTxt.rect.y+50)

    def draw (self, screen):
        self.overImg.draw(screen)
        self.scoreTxt.draw(screen)
        self.topScoreTxt.draw(screen)
        for txt in self.scoreList:
            txt.draw(screen)
        self.retryImg.draw(screen)

    def updateScore (self, newScore):
        self.score = newScore
        self.scoreTxt.updateText(f"Score: {int(self.score)}")

    def updateScoreList(self, topScores):
        lineGap = 50
        txt = str(topScores[0][0])+" = "+str(topScores[0][1])
        refScore = Text(txt, self.screenWidth//2, self.topScoreTxt.rect.y+50)
        self.scoreList.append(refScore)
        for i in range(1, len(topScores)):
            txt = str(topScores[i][0])+" = "+str(topScores[i][1])
            self.scoreList.append(Text(txt, self.screenWidth//2, self.scoreList[i-1].rect.y+lineGap))

