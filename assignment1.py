import numpy as np



##Class node, we use this to store each box in the grid as an object##
class node:
	"""docstring for ClassName"""
	def __init__(self,data, x, y, fn):
		self.data = data
		self.x = x
		self.y = y
		self.fn = fn

	def set_xy(self, x, y):
		self.x = x
		self.y = y

def pathfinding(input_filename, optimal_path_filename, explored_list_filename):
  # input_filename contains a CSV file with the input grid
  # optimal_path_filename is the name of the file the optimal path should be written to
  # explored_list_filename is the name of the file the list of explored nodes should be written to

  #store the grid as a mxn grid#
  grid = np.genfromtxt(input_filename, dtype=str)
  for i in range(len(grid)):
  	for j in range(len(grid[i])):
  		grid[i][j] = grid[i][j].replace(',','')

  #global varibales
  m = len(grid)
  n = len(grid[0])

  #create frontier and explored lists#
  frontier = []
  explored = []


  currpathcost = 0
  currnode = node(grid[0][0],0,0,0)
  frontier.append(currnode)
  while True:
  	left = currnode.x-1
  	right = currnode.x+1
  	up = currnode.y-1
  	down = currnode.y+1


  	#add all adjacent nodes to currnode to frontier#
  	if left > 0:
  		if grid[currnode.y][currnode.x-1] == 'G':
  			left_node = node(grid[currnode.y][currnode.x-1],currnode.x-1,currnode.y,0)
  			frontier.append(left_node)

  		elif grid[currnode.y][currnode.x-1] != 'X':
  			left_node = node(grid[currnode.y][currnode.x-1],currnode.x-1,currnode.y,int(grid[currnode.y][currnode.x-1])+currpathcost)
  			frontier.append(left_node)


  	if right < n:
  		if grid[currnode.y][currnode.x+1] == 'G':
  			right_node = node(grid[currnode.y][currnode.x+1],currnode.x+1,currnode.y,0)
  			frontier.append(right_node)

  		elif grid[currnode.y][currnode.x+1] != 'X' and grid[currnode.y][currnode.x+1] != 'V':
  			right_node = node(grid[currnode.y][currnode.x+1],currnode.x+1,currnode.y,int(grid[currnode.y][currnode.x+1])+currpathcost)
  			frontier.append(right_node)


  	if up > 0:
  		if grid[currnode.y-1][currnode.x] == 'G':
  			up_node = node(grid[currnode.y-1][currnode.x],currnode.x,currnode.y-1,0)
  			frontier.append(up_node)

  		elif grid[currnode.y-1][currnode.x] != 'X':
  			up_node = node(grid[currnode.y-1][currnode.x],currnode.x,currnode.y-1,int(grid[currnode.y-1][currnode.x])+currpathcost)
  			frontier.append(up_node)


  	if down < m:
  		if grid[currnode.y+1][currnode.x] == 'G':
  			down_node = node(grid[currnode.y+1][currnode.x],currnode.x,currnode.y+1,0)
  			frontier.append(down_node)

  		elif grid[currnode.y+1][currnode.x] != 'X':
  			down_node = node(grid[currnode.y+1][currnode.x],currnode.x,currnode.y+1,int(grid[currnode.y+1][currnode.x])+currpathcost)
  			frontier.append(down_node)

  	#check if currnode is goal state, if goal state then break#
  	if currnode.data == 'G':
  		break

  	#remove currnode from frontier and add to explored node#
  	frontier.remove(currnode)
  	explored.append(currnode)

  	#set the currnode to the node with minimum cost#
  	currnode = frontier[0]
  	for i in range(len(frontier)):
  		if frontier[i].fn < currnode.fn:
  			currnode = frontier[i]


  	currpathcost+= currnode.fn

  for i in range(len(explored)):
    print("(", explored[i].x, ", ", explored[i].y, ")", " Pathcost: ", explored[i].fn)














  	

  	
  	


  return 0





pathfinding("input.txt", 1,1)