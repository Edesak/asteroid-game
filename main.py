import os

import pygame
from constants import *
from player import Player

#Delete this line if on windows
os.environ["SDL_VIDEODRIVER"]="x11"

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Initialize pygame
    pygame.init()
    
    #Seting up gaming clock
    clock = pygame.time.Clock()
    dt = 0
    #set screen resolution 
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    #Creating groups so we can create multiple callings in one for loop
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"black")

        for entity in updatable:
            entity.update(dt)
        
        for entity in drawable:
            entity.draw(screen)

        #Determin the max FPS for game (60) and time between frames
        dt = clock.tick(60)
        dt = dt/1000
        pygame.display.update()

if __name__ == "__main__":
    main()