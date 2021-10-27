import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption("Ta-Te-Ti")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    surface.fill((0,0,0))
    pygame.display.flip()