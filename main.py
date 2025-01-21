import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)

    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for element in updatable:
            element.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        # handle screen refresh to 60 fps to use less resources
        dt = clock.tick(60) / 1000
        
        for element in drawable:
            element.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()