import pygame
import os

from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'
surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Server_ Tic-tac-toe')
import threading
import socket

def create_thread(target):
	thread = threading.Thread(target = target)
	thread.daemon = True
	thread.start()

HOST = '127.0.0.1'

PORT = 65432
connection_estableshed = False
conn, addr = None, None
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

def receive_data():
	global turn
	while True:
		data = conn.recv(1024).decode()
		data = data.split('-')
		x,y = int(data[0]),int(data[1])
		if data[2] == 'yourturn':
			turn = True
		if data[3]== 'False':
			grid.game_over = True
		if grid.get_cell_value(x, y) == 0:
			grid.set_cell_value(x, y, 'O')
		#print(data)

def waiting_for_connection():
	global connection_estableshed, conn, addr
	conn, addr = sock.accept() 
	print('client is connected')
	connection_estableshed = True
	receive_data()

create_thread(waiting_for_connection)

grid = Grid()

#grid.set_cell_value(1,1,'x')

#grid.print_grid()

running = True
player = 'X'
turn = True
playing = 'True'

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and connection_estableshed:
			if pygame.mouse.get_pressed()[0]:
				if turn and not grid.game_over:
					pos = pygame.mouse.get_pos()
					cellX, cellY = pos[0] // 200, pos[1] // 200				
					grid.get_mouse(cellX,cellY, player)
					if grid.game_over:
						playing = 'False'
					send_data = '{}-{}-{}-{}'.format(cellX,cellY, 'yourturn', playing).encode()
					conn.send(send_data)
					turn = False
					
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and grid.game_over:
				grid.clear_grid()
				grid.game_over = False
				playing = 'True'
			elif event.key == pygame.K_ESCAPE:
				running = False
	surface.fill((0,0,0))
	
	grid.draw(surface)

	pygame.display.flip()
	