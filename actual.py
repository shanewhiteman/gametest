import pygame
import sys

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Shane Game")
WINDOW_SIZE = (500,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

# def quit():
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

font = pygame.font.SysFont(None, 20)

click = False

def framerate():
    clock = pygame.time.Clock()
    pygame.display.update()
    clock.tick(60)

def draw_text(text, font, color, surface, x, y):
    textobject = font.render(text, 1, color)
    textrect = textobject.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobject, textrect)

def menu():

    while True:

        screen.fill((0,0,0))

        draw_text('main_menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        #postion of buttons
        button_1 = pygame.Rect(350, 300, 100, 50) # green
        button_2 = pygame.Rect(50, 300, 100, 50) # red block

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        framerate()
        
        pygame.draw.rect(screen, (0, 255, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        framerate()

def game():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        framerate()

def options():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        framerate()

def main():
    menu()

main()