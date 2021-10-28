import pygame
import os

letraX = pygame.image.load(os.path.join('res','letraX.png'))
letraO = pygame.image.load(os.path.join('res','letraO.png'))

class Grid:
	#Constructores
	#region 
	def __init__(self):
		self.grid_line = [((0,200), (600,200)), # Primera linea Horizontal
						  ((0,400), (600,400)), # Segunda linea Horizontal
						  ((200,0), (200,600)), # Primera linea Vertical
						  ((400,0), (400,600))] # Segunda linea Vertical
	
		self.grid = [[0 for x in range(3)] for y in range(3)]

		self.switch_player = True

		#print(self.grid)

	def draw(self, surface):
		for line in self.grid_line:
			pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)

		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				if self.get_cell_value(x,y) == 'X':
					surface.blit(letraX,(x*200, y*200))
				elif self.get_cell_value(x,y) == 'O':
					surface.blit(letraO,(x*200, y*200))

	def get_cell_value(self, x, y):
		return self.grid[y][x]

	def set_cell_value(self, x, y, value):
		self.grid[y][x] = value

	def get_mouse(self, x, y, player):
		if self.get_cell_value(x,y) == 0:
			self.switch_player = True
			if player == 'X':
				self.set_cell_value(x,y,'X')
			elif player == 'O':
				self.set_cell_value(x,y,'O')
		else:
			self.switch_player = False

	def print_grid(self):
		for row in self.grid:
			print(row)
	
	#endregion