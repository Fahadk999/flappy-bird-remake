import pygame
from src.gamestates.playstate import PlayState

pygame.init()

WIDTH, HEIGHT = 1080, 720 

STATEMENU = "MENU"
STATEPLAY = "PLAY"

currState = STATEPLAY

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()

playstate = PlayState(WIDTH, HEIGHT)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill(pygame.Color("lightblue"))

    keys = pygame.key.get_pressed()
    # GameStates
    if currState == STATEPLAY:
        playstate.update(events)
        playstate.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

    