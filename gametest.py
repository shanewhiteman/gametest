import pygame
import sys

clock = pygame.time.Clock() # set up the clock
 
from pygame.locals import *

pygame.init()
 
pygame.display.set_caption('Shane Game') # set the window name
 
WINDOW_SIZE = (500,400) # set up window size
 
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # init screen
 
player_image = pygame.image.load('files/player.png')
 
moving_right = False
moving_left = False
 
player_location = [50,50]
player_y_momentum = 0

# rectangle(rect) for player pos
player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)
 
while True: # game loop

    screen.fill((146,244,255)) # clear screen by filling it with blue
 
    screen.blit(player_image,player_location) # render player
 
    # bounce to rect of bottom
    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    # right left movement
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    
    # update rect to player position
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]
 
    # test rect for collisions
    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen,(255,0,0),test_rect)
    else:
        pygame.draw.rect(screen,(0,0,0),test_rect)
    
    for event in pygame.event.get(): # event loop
        
        if event.type == QUIT: # check for window quit
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
 
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps