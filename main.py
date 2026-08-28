import pygame
from src.gamestates.menustate import MenuState
from src.gamestates.playstate import PlayState
from src.gamestates.overstate import OverState
from src.database import db_manager as db

pygame.init()

WIDTH, HEIGHT = 1080, 720 

STATEMENU = "MENU"
STATEPLAY = "PLAY"
STATEOVER = "OVER"

currState = STATEPLAY

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()

db.initDB()
menustate = MenuState(WIDTH, HEIGHT)
playstate = PlayState(WIDTH, HEIGHT)
overstate = OverState(WIDTH, HEIGHT) 

running = True
while running:
    dt = clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r and currState == STATEOVER:
                currState = STATEPLAY
                playstate.resetGame()


    screen.fill(pygame.Color("lightblue"))

    keys = pygame.key.get_pressed()
    # GameStates
    if currState == STATEMENU:
        currState = menustate.update(events, currState)
        menustate.draw(screen)
    elif currState == STATEPLAY:
        currState = playstate.update(events, dt, currState)
        playstate.draw(screen)
        if currState == STATEOVER:
            score = int(playstate.score)
            overstate.updateScore(score)
            db.saveScore(score)
            topScores = db.getScores()
            overstate.updateScoreList(topScores)
    elif currState == STATEOVER:
        playstate.draw(screen)
        overstate.draw(screen)

    pygame.display.flip()

pygame.quit()

    
