import pygame
pygame.init()
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    pygame.display.flip()


if __name__ == "__main__":
    main()