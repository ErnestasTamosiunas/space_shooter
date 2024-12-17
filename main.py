# this allows to use code from open-source
# pygame library throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

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
    shots = pygame.sprite.Group()

    # Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Player object
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Shots
    Shot.containers = (shots, updatable, drawable)
    
    # Score
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)
    score = Score()

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

            for shot in shots:
                if asteroid.colided(shot):
                    score.increase_score()
                    shot.kill()
                    asteroid.split()

        # Filling the screen with solid black
        screen.fill((0, 0, 0))

        # Drawables group
        for obj in drawable:
            obj.draw(screen)

        # Score represented in white color
        score_text = font.render(f"Score: {score.get_score()}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Refreshing the screen
        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

# Ensures that main() is only called when this file is run directly
if __name__ == "__main__":
    main()