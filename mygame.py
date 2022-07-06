import pygame
import random
from pygame.locals import *

pygame.init()
w = 1000
h = 500
red = (255, 0, 0)
col = (255, 255, 255)
col1 = (228, 0, 25)
sec = 8
pygame.time.set_timer(USEREVENT + 1, 1000)
SOUND = True
COLORR = (255, 0, 0)

bsound = pygame.mixer.Sound("assets/sounds/background.wav")
bsound.play()


screen = pygame.display.set_mode((w, h))
settings = pygame.image.load("assets/images/settings.png")
settings = pygame.transform.scale(settings, (60, 60))
pic = pygame.image.load("assets/images/back2.jpeg")
pic = pygame.transform.scale(pic, (1000, 500))
tar = pygame.image.load("assets/images/pritsel.png")
tar = pygame.transform.scale(tar, (100, 100))
gun = pygame.image.load("assets/images/gun_1.png")
blood = pygame.image.load("assets/images/zombie_blood.png")
gsound = pygame.mixer.Sound("assets/sounds/shot_sound.wav")

GSOND = True

def time(sec):
    font = pygame.font.SysFont('Ariel', 40)
    text = font.render('time left : ' + str(sec), True, col)
    screen.blit(text, (w - 200, 10))


def start_game():
    f = True
    start = pygame.image.load("assets/images/start.png")
    start = pygame.transform.scale(start, (300, 200))
    start_rec = pygame.Rect(w / 2 - 150, h / 2 - 100, start.get_width(), start.get_height())
    settings_rec = pygame.Rect(0, 0, 60, 60)
    while f:
        mx, my = pygame.mouse.get_pos()
        pointer = pygame.Rect(mx, my, 1, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rec.colliderect(pointer):
                    f = False
                    game()

                if settings_rec.colliderect(pointer):
                    f = False
                    settings1()

        screen.blit(pic, (0, 0))
        screen.blit(settings, (0, 0))
        screen.blit(start, (w / 2 - 150, h / 2 - 100))
        pygame.display.update()


def settings1():
    global COLORR
    global GSOND
    f = True
    set = pygame.image.load("assets/images/set.png")
    set = pygame.transform.scale(set, (700, 200))

    close = pygame.image.load("assets/images/close.png")
    close = pygame.transform.scale(close, (20, 20))
    while f:
        pygame.display.update()
        screen.blit(set, (100, 100))
        screen.blit(close, (730, 145))
        font = pygame.font.SysFont('Ariel', 40)
        text = font.render('Настройки', True, (255, 255, 255))
        screen.blit(text, (230, 120))
        font = pygame.font.SysFont('Ariel', 40)
        text = font.render('Звук ', True, (0, 0, 0))
        screen.blit(text, (240, 195))
        pygame.draw.rect(screen, (0, 0, 0), (320, 200, 15, 15))
        pygame.draw.rect(screen, (255, 255, 255), (322, 202, 10, 10))
        pygame.draw.rect(screen, COLORR, (324, 204, 5, 5))
        sound_rec = pygame.Rect(322, 202, 10, 10)
        close_rec = pygame.Rect(730, 145, 20, 20)
        px, py = pygame.mouse.get_pos()
        pointer1 = pygame.Rect(px, py, 1, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sound_rec.colliderect(pointer1):
                    if COLORR == (255, 0, 0):
                        COLORR = (255, 255, 255)
                        pygame.draw.rect(screen, COLORR, (324, 204, 5, 5))
                        bsound.stop()
                        GSOND = False
                    else:
                        COLORR = (255, 0, 0)
                        pygame.draw.rect(screen, COLORR, (324, 204, 5, 5))
                        bsound.play()
                        GSOND = True

                if close_rec.colliderect(pointer1):
                    f = False
                    screen.blit(pic, (0, 0))
                    over()


def over():
    f = True
    while f:
        font = pygame.font.SysFont('Ariel', 80)
        text = font.render('GAME OVER !! ', True, col1)
        restart = pygame.image.load("assets/images/restart.png")
        restart = pygame.transform.scale(restart, (284, 60))
        screen.blit(text, (w / 2 - 200, h / 2 - 60))
        screen.blit(restart, (w / 2 - 150, h / 2))
        pygame.display.update()
        restart_rec = pygame.Rect(w / 2 - 150, h / 2, restart.get_width(), restart.get_height())
        settings_rec = pygame.Rect(0, 0, 60, 60)
        px, py = pygame.mouse.get_pos()
        pointer = pygame.Rect(px, py, 1, 1)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rec.colliderect(pointer):
                    f = False
                    game()

                if settings_rec.colliderect(pointer):
                    f = False
                    settings1()






def score(counter):
    font = pygame.font.SysFont(None, 40)
    text = font.render('score : ' + str(counter), True, red)
    screen.blit(text, (w - 200, 40))


def game():
    sec = 10
    w = 1000
    h = 500
    z0 = pygame.image.load("assets/images/in4.png")
    z0 = pygame.transform.scale(z0, (300, 200))
    z1 = pygame.image.load("assets/images/in1.png")
    z1 = pygame.transform.scale(z1, (300, 200))
    z2 = pygame.image.load("assets/images/in2.png")
    z2 = pygame.transform.scale(z2, (300, 200))
    z3 = pygame.image.load("assets/images/in3.png")
    z3 = pygame.transform.scale(z3, (200, 250))
    z4 = pygame.image.load("assets/images/in5.png")
    z4 = pygame.transform.scale(z4, (300, 250))
    zlist = [z1, z2, z3, z0, z4]
    zimg = random.choice(zlist)
    zx = random.randint(0, w - 300)
    zy = random.randint(250, h - 250)
    f = True
    counter = 0

    while f:
        mx, my = pygame.mouse.get_pos()
        zrec = pygame.Rect(zx, zy, zimg.get_width(), zimg.get_height())
        point = pygame.Rect(mx, my, tar.get_width(), tar.get_height())
        settings_rec = pygame.Rect(0, 0, 60, 60)
        pointer = pygame.Rect(mx, my, 1, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT + 1:
                sec -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if GSOND:
                    gsound.play()
                if zrec.colliderect(point):
                    zx = random.randint(0, w - 200)
                    zy = random.randint(0, h - 300)
                    zimg = random.choice(zlist)
                    counter += 1

                if settings_rec.colliderect(pointer):
                    f = False
                    settings1()
        if sec == 0:
            f = False
            over()
            break

        screen.blit(pic, (0, 0))
        screen.blit(zimg, (zx, zy))
        screen.blit(settings, (0, 0))
        screen.blit(tar, (mx - 48, my - 48))
        score(counter)
        time(sec)
        screen.blit(gun, (mx, h - 250))
        pygame.display.update()


start_game()
