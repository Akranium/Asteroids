import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from player import Player

def main():
    # Basic logging
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initializing variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0 # Delta time

    # Making groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Adding classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Initializing group members
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    while True:
        # Logging
        log_state()

        # Exit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Delta time
        dt = clock.tick(FPS) / 1000

        # Updating
        updatable.update(dt)

        # Drawing
        screen.fill("black")
        for drawmember in drawable:
            drawmember.draw(screen)


        # Flipping
        pygame.display.flip()


if __name__ == "__main__":
    main()
