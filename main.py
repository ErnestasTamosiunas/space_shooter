# this allows to use code from open-source
# pygame library throughout this file
import pygame
from constants import *

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

    # Game loop
    while True:
        # Adding game loop window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Filling the screen with solid black
        pygame.Surface.fill(screen, (0, 0, 0))

        # Refreshing the screen
        pygame.display.flip()

        dt = clock.tick(FPS)
        #dt = clock.tick(60) / 1000

# Ensures that main() is only called when this file is run directly
if __name__ == "__main__":
    main()