import random
import pygame
import sys
from pygame import mixer
from pygame.time import delay

pygame.init()
mixer.init()

screen = pygame.display.set_mode((1200, 800))
pool = pygame.image.load('pool.png')
pool = pygame.transform.scale(pool, (1200, 800))
myfont = pygame.font.SysFont("Comic Sans", 75)

player = pygame.image.load('player.png')

mixer.music.load('potato.mp3')
food_sound = mixer.Sound('food.mp3')

wall = pygame.image.load('wall.png')

help = pygame.image.load('help.png')

mainmenu = pygame.image.load('mainmenu.png')
mainmenu = pygame.transform.scale(mainmenu, (1200, 800))

burger_image = pygame.image.load('burger.png')
burger_image = pygame.transform.scale(burger_image, (150, 150))

youlose_image = pygame.image.load('youlose.png')
youlose_image = pygame.transform.scale(youlose_image, (1200, 800))
m = 1

def spawnburger():
    global burger_rect
    burger_x = random.randint(200, 1000)
    burger_y = random.randint(100, 700)
    burger_rect = pygame.Rect(burger_x, burger_y, 2, 2)

def playgame():
    gravity = 200
    mixer.music.set_volume(0.7)
    food_sound.set_volume(1)
    global score, player, xr, xl, wlx, wall
    wlx = 100
    wall = pygame.transform.scale(wall, (wlx, 800))
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    y = y - gravity

        if x + 375 >= xr:
            pr = 0
            pl = 1
        if x + 25 <= xl:
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
            if score < 30:
                gravity -= 5
            else:
                gravity -= 1
            spawnburger()
            food_sound.play() 

        screen.blit(pool, (0, 0))
        screen.blit(player, (x, y))
        screen.blit(burger_image, burger_rect.topleft)
        screen.blit(wall, (0, 0))
        screen.blit(wall, (1100, 0))
        scoregui = myfont.render("Score = " + str(score), 1, (0, 0, 0))
        screen.blit(scoregui, (5, 10))

        delay(25)
        pygame.display.update()

while m == 1:
    screen.blit(mainmenu, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                Ler = 1
                while Ler == 1:
                    screen.blit(help, (0, 0))
                    pygame.display.update()
                    delay(100)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            playgame()
            else:
                playgame()
