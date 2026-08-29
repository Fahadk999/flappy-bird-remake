import pygame
from src.ui.text import Text
from src.ui.imageloader import LoadImage
from src.soundloader import LoadSound
from abs_path import absPath

class OverState:
    def __init__(self, screenWidth, screenHeight, score=0) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.score = score
        overPath = absPath("assets/gameover.png")
        retryPath = absPath("assets/retry.png")
        menuPath = absPath("assets/menu.png")
        scorePath = absPath("assets/score.png")
        buttonSfxPath = absPath("assets/sounds/buttonclick.wav")
        self.fontPath = absPath("assets/fonts/customfont.otf")

        self.overImg = LoadImage(overPath, 1, screenWidth//2, screenHeight//5)
        self.scoreTxt = Text(int(self.score), screenWidth//2, screenHeight//3, self.fontPath, 35)
        self.scoreList = [] 
        self.retryImg = LoadImage(retryPath, 1, screenWidth//2, screenHeight-screenHeight//4)
        self.menuImg = LoadImage(menuPath, 1, screenWidth//2, screenHeight-screenHeight//6)
        self.buttonSound = LoadSound(buttonSfxPath, 0.5)
        self.scoreImg = LoadImage(scorePath, 1, screenWidth//2, screenHeight//3)

        self.topScoreTxt = Text("Top Scores", screenWidth//2, self.scoreTxt.rect.y+65, self.fontPath, 45, pygame.Color("Yellow"))

    def draw (self, screen):
        self.overImg.draw(screen)
        self.scoreTxt.draw(screen)
        self.scoreImg.draw(screen)
        self.topScoreTxt.draw(screen)
        for txt in self.scoreList:
            txt.draw(screen)
        self.retryImg.draw(screen)
        self.menuImg.draw(screen)

    def update(self, dt, events, currState, playstate):
        self.retryImg.idleAnimationY(dt, 1, 50)
        self.menuImg.idleAnimationY(dt, -1, 50)

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    self.buttonSound.play()
                    playstate.resetGame()
                    currState = "PLAY"
                if e.key == pygame.K_m:
                    self.buttonSound.play()
                    playstate.resetGame()
                    currState = "MENU"

        return currState

    def updateScore (self, newScore):
        self.scoreList.clear()
        self.score = newScore
        self.scoreTxt.updateText(int(self.score))
        totalWidth = self.scoreImg.rect.width+self.scoreTxt.rect.width
        scorePosX = self.scoreImg.rect.x+self.scoreImg.rect.width
        self.scoreImg.rect.x = (self.screenWidth//2)-totalWidth//2
        self.scoreTxt.rect.x = self.scoreImg.rect.x+self.scoreImg.rect.width

    def updateScoreList(self, topScores):
        lineGap = 65
        txt = str(topScores[0][0])+" = "+str(topScores[0][1])
        refScore = Text(txt, self.screenWidth//2, self.topScoreTxt.rect.y+70, self.fontPath, 35)
        self.scoreList.append(refScore)
        for i in range(1, len(topScores)):
            txt = str(topScores[i][0])+" = "+str(topScores[i][1])
            self.scoreList.append(Text(txt, self.screenWidth//2, self.scoreList[i-1].rect.y+lineGap, self.fontPath, 35))

