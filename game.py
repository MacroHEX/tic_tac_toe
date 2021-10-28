import pygame
import os

from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe')

grid = Grid()

#grid.set_cell_value(1,1,'x')

grid.print_grid()

running = True

player = 'X'

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# print (pygame.mouse.get_pressed())
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				#print(pos[0] // 200, pos[1] // 200)
				grid.get_mouse(pos[0] // 200, pos[1] // 200,player)
				if grid.switch_player:
					if player == 'X':
						player = 'O'
					else:
						player = 'X'

				grid.print_grid()
	surface.fill((0,0,0))
	
	grid.draw(surface)

	pygame.display.flip()
	