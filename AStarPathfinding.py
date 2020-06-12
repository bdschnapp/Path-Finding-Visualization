from joystick import DualShock4
from matrix import Matrix
import threading
import pygame
import sys

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')



def inputThread(lock):
	try:
		while running:
			lock.acquire()
			try:
				ds4Input.update()
			finally:
				lock.release()
			ds4Input.tick(20)
	except:
		print("Controller not connected, please connect a controller")

	finally:
		pass

def printSquare(x,y,screen,color):
	pygame.draw.rect(screen, BLACK, ((50*x),(50*y),(50),(50)), 2)
	pygame.draw.rect(screen, color, ((50*x+2),(50*y+2),(48),(48)), 0)

def updateScreen(screen, Matrix, xPos, yPos):
	
	for i in range(len(Matrix)):
		for j in range(len(Matrix[i])):
			if Matrix[i][j] == 0:
				color = WHITE
			elif Matrix[i][j] == 1:
				color = RED
			elif Matrix[i][j] == 2:
				color = BLUE
			elif Matrix[i][j] == 3:
				color = GREEN
			printSquare(j,i,screen,color)
	pygame.draw.rect(screen, YELLOW, ((50*xPos+20),(50*yPos+20),(10),(10)), 0)
	
	pygame.display.flip()



if len(sys.argv) == 3:
	w = int(sys.argv[1])
	h = int(sys.argv[2])
else:
	w = 1200
	h = 700



#rounds width and height to nearest 50 pixels
w = w - (w % 50)
h = h - (h % 50)

pygame.init()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("AStar Pathfinding")
clock = pygame.time.Clock()

Rlock = threading.RLock()
ds4Input = DualShock4(0)
ds4Input.update()

inputDecon = False
screen.fill(WHITE)


threading._start_new_thread(inputThread, RLock)


running = True
setUp = True
startPathfinding = False

xPos = 0
yPos = 0
Matrix = Matrix(w, h)

while running:
	while setUp:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT) or (ds4Input.ps4 == 1):
				running = False
				setup = False
				startPathFinding = False

		#ds4Input.update()

		#updates cursor position
		if ds4Input.lsHorizontal > .5:
			xPos = (xPos + 1)%(len(Matrix[yPos]))
			#while ds4Input.lsHorizontal > .5:
			#	pass
		if ds4Input.lsHorizontal < -.5:
			xPos = (xPos - 1)%(len(Matrix[yPos]))
			#while ds4Input.lsHorizontal < -.5:
			#	pass
		if ds4Input.lsVertical > .5:
			yPos = (yPos + 1)%(len(Matrix))
			#while ds4Input.lsVertical > .5:
			#	pass
		if ds4Input.lsVertical < -.5:
			yPos = (yPos - 1)%(len(Matrix))
			#while ds4Input.lsVertical < -.5:
			#	pass


		#reacts to button inputs and updates Matrix accordingly
		
		#x is for toggling between a blocked node and an open node
		if ds4Input.x == 1:
			if Matrix[yPos][xPos] == 1:
				Matrix[yPos][xPos] = 0
			else: 
				Matrix[yPos][xPos] = 1
			#while ds4Input.x == 1:
			#	pass
		
		#square is for setting the starting position
		if ds4Input.square == 1:
			for y in range(len(Matrix)):
				for x in range(len(Matrix[y])):
					if Matrix[y][x] == 2:
						Matrix[y][x] = 0
			if Matrix[yPos][xPos] == 3:
				Matrix[0][0] = 3
			Matrix[yPos][xPos] = 2
			#while ds4Input.square == 1:
			#	pass
		
		#circle is for setting the end position
		if ds4Input.circle == 1:
			for y in range(len(Matrix)):
				for x in range(len(Matrix[y])):
					if Matrix[y][x] == 3:
						Matrix[y][x] = 0
			if Matrix[yPos][xPos] == 2:
				Matrix[0][0] = 2
			Matrix[yPos][xPos] = 3
			#while ds4Input.circle == 1:
			#	pass
		
		#triangle starts the pathfinding sequence
		if ds4Input.triangle == 1: 
			pass
		
		#updates the screen
		updateScreen(screen, Matrix, xPos, yPos)
		print((xPos,yPos))
		clock.tick(20)

	while startPathfinding:
		pass
pygame.quit()
sys.exit()