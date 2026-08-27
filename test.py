import pygame

pygame.init()

WIDTH, HEIGHT = 1080, 720 

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()

img = pygame.image.load("assets/bird.png").convert_alpha()
img = pygame.transform.smoothscale(img, (60, 38))
pivot = (100,300)
origRect = img.get_rect(center=pivot)
angle = 0

running = True
while running:
    dt = clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill(pygame.Color("lightblue"))
    angle = (angle-2)%360

    rotatedImg = pygame.transform.rotate(img,angle)
    rotatedRect = rotatedImg.get_rect(center=pivot)

    screen.blit(rotatedImg, rotatedRect)

    pygame.display.flip()

pygame.quit()

    
