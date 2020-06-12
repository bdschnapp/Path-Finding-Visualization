class Matrix(object):

	def __init__(self, w, h):
		self.matrix = [[0 for x in range(int(w/50))] for y in range(int(h/50))]
	
	#__setitem__ method is redundant because default list __setitem__ applies

	def __getitem__(self, i):
		#try:
		return self.matrix[i]
		#except IndexError:
		#	if i < 0:
		#		return self.matrix[0]
		#	if i > len(self.matrix):
		#		return self.matrix[len(self.matrix)]

	def __len__(self):
		return len(self.matrix)

	def pathfindingRecur(self, yPos, xPos, visited = []): #matirx[int][int], int xPos, int yPos
		xPlus = [] #right
		xMinus = [] #left
		yPlus = [] #down
		yMinus = [] #up
		
		tempVisited = visited
		tempVisited.append((yPos,xPos))
		
		#finds the shortest path from each adjacent node to the end, or returns the curent node's coordinates if it is adjacent to the end node
		if not((xPos == 0) or (matrix[yPos][xPos-1] == 1) or (((yPos),(xPos-1)) in visited)): #left
			if matrix[yPos][xPos-1] == 3: #base case 
				return [(yPos,xPos)]
			xMinus = pathfindingRecur(matrix, yPos, (xPos-1), tempVisited) 
	
		if not((yPos == 0) or (matrix[yPos-1][xPos] == 1) or (((yPos-1),(xPos)) in visited)): #up
			if matrix[yPos-1][xPos] == 3: #base case 
				return [(yPos,xPos)]
			yMinus = pathfindingRecur(matrix, (yPos-1), xPos, tempVisited)
	
		if not((xPos == len(matrix[yPos])) or (matrix[yPos][xPos+1] == 1) or (((yPos),(xPos+1)) in visited)): #right
			if matrix[yPos][xPos+1] == 3: #base case 
				return [(yPos,xPos)]
			xPlus = pathfindingRecur(matrix, yPos, (xPos+1), tempVisited)
	
		if not((yPos == len(matrix)) or (matrix[yPos+1][xPos] == 1) or (((yPos+1),(xPos)) in visited)): #down
			if matrix[yPos+1][xPos] == 3: #base case 
				return [(yPos,xPos)]
			yPlus = pathfindingRecur(matrix, (yPos+1), xPos, tempVisited)

		#calculates the shortest (non zero) path out of the paths returned by the adjacent nodes
		temp = []
		temp.append(xPlus)
		temp.append(xMinus)
		temp.append(yPlus)
		temp.append(yMinus)

		#removes zero length paths
		temp = [i for i in temp if len(i) != 0]
		
		#sorts remaining 
		for i in range(len(temp)-1):
			if len(temp[i]) < len(temp[i+1]):
				swap = temp[i]
				temp[i] = temp[i+1]
				temp[i+1] = swap
						
		#returns the shortest path
		return temp[len(temp)]





