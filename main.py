import os
from sys import exit
import pygame # type: ignore
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
#Delete this line if on windows
os.environ["SDL_VIDEODRIVER"]="x11"

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Initialize pygame
    pygame.init()
    pygame.font.init()
    GAME_FONT = pygame.freetype.Font("./DepartureMono-Regular.otf", 22)
    #Seting up gaming clock
    clock = pygame.time.Clock()
    dt = 0
    #set screen resolution 
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    #Creating groups so we can create multiple callings in one for loop
    updatable, drawable, asteroids, bullets = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    Shot.containers = (updatable, drawable, bullets)

    p = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    af = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"black")
        GAME_FONT.render_to(screen, (40, 30), f"Score: {p.score}", (255, 255, 0))
        for entity in updatable:
            entity.update(dt)
        
        for entity in drawable:
            entity.draw(screen)

        #Determin the max FPS for game (60) and time between frames
        dt = clock.tick(60)
        dt = dt/1000
        pygame.display.update()

        for entity in asteroids:
            if not entity.colisionCheck(p):
                print("Gameru Overu")
                exit()
            for bullet in bullets:
                if not entity.colisionCheck(bullet):
                    bullet.kill()
                    p.add_score(entity.split())
if __name__ == "__main__":
    main()