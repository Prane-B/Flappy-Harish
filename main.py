import random
import pygame
import sys

from pygame import K_SPACE
from pygame.time import delay


pygame.init()


screen = pygame.display.set_mode((1200, 800))
pool = pygame.image.load('pool.png')
pool = pygame.transform.scale(pool, (1200, 800))
myfont = pygame.font.SysFont("monospace", 40 )

player = pygame.image.load('player.png')

mainmenu = pygame.image.load('mainmenu.png')
mainmenu = pygame.transform.scale(mainmenu, (1200, 800))

burger_image = pygame.image.load('burger.png')
burger_image = pygame.transform.scale(burger_image, (150, 150))

youlose_image = pygame.image.load('youlose.png')
youlose_image = pygame.transform.scale(youlose_image, (1200, 800))
m = 1

def spawnburger():
    global burger_rect
    burger_x = random.randint(0, 1100)
    burger_y = random.randint(100, 700)
    burger_rect = pygame.Rect(burger_x, burger_y, 2, 2)


def playgame():
    global score, player, xr, xl
    massx = 250
    massy = 200
    score = 0
    x = 400
    y = 200
    pr = 1
    pl = 0
    spawnburger()
    xr = 1200
    xl = 0
    run = True
    while run:
        player_rect = pygame.Rect(x, y, massx, massy)
        player = pygame.transform.scale(player, (massx, massy))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    y = y - 200


        if x + massx >= xr:
            pr = 0
            pl = 1
        if x <= xl:
            pr = 1
            pl = 0
        if pr == 1:
            x = x + 10
        if pl == 1:
            x = x - 10

        if y > 750:
            L = 1
            while L == 1:
                screen.blit(youlose_image, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_r:
                            playgame()

        y = y + 10
        player_rect.topleft = (x, y)

        if player_rect.colliderect(burger_rect):
            score += 1
            massx += 25
            massy += 25
            spawnburger()


        screen.blit(pool, (0, 0))
        screen.blit(player, (x, y))
        screen.blit(burger_image, burger_rect.topleft)
        scoregui = myfont.render("Score = " + str(score), 1, (0, 0, 0))
        screen.blit(scoregui, (5, 10))

        delay(25)
        pygame.display.update()

while m == 1:
    screen.blit(mainmenu, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            playgame()

