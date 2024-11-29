# this allows to use code from open-source
# pygame library throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Setting up a screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Setting FPS
    clock = pygame.time.Clock()
    dt = 0

    # Setting groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Player object
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Adding game loop window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Updatables group
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.colided(player):
                print("Game over!")
                exit()

        # Filling the screen with solid black
        screen.fill((0, 0, 0))

        # Drawables group
        for obj in drawable:
            obj.draw(screen)

        #player.draw(screen)
        #player.update(dt)

        # Refreshing the screen
        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

# Ensures that main() is only called when this file is run directly
if __name__ == "__main__":
    main()