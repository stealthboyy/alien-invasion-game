# MAKING A PYGAME WINDOW WITH A BLUE BACKGROUND

import sys

import pygame


class BlueSky:
    """A class to develop a game with a blue background"""
    def __init__ (self):
        """Initialize the attributes of the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,500))
        pygame.display.set_caption("Blue Sky")

        self.bg_color = (0, 250, 230)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboards and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = BlueSky()
    ai.run_game()