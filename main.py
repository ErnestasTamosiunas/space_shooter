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

    # Game loop
    while True:
        # Filling the screen with solid black
        pygame.Surface.fill(screen, color="black") # Experimenting

        # Refreshing the screen
        pygame.display.flip()

# Ensures that main() is only called when this file is run directly
if __name__ == "__main__":
    main()