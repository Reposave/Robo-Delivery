import sys
import pprint

def main():
	print("Welcome")
	if(len(sys.argv)<3):
		print("Please specify environment dimensions. ValueIteration.py width height")
		
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	
	startx = 0
	starty = 0
	
	endx = 1
	endy = 1
	
	ldmine_num = 1
	
	g = 0.5 #discount factor.
	
	if(len(sys.argv)>3):
		for i in range(3,len(sys.argv)):
			if(sys.argv[i] == "-start"):
				startx = int(sys.argv[i+1])
				starty = int(sys.argv[i+2])
			
			if(sys.argv[i] == "-end"):
				endx = int(sys.argv[i+1])
				endy = int(sys.argv[i+2])
				
			if(sys.argv[i] == "-k"):
				ldmine_num = int(sys.argv[i+1])
				
			if(sys.argv[i] == "-gamma"):
				g = float(sys.argv[i+1]) 
				
				
	envment=[[0]*width for _ in range (height)]
	rewards=[[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)] #All set to 0.
	
	pprint.pprint(rewards)
	print()
	
	envment[endx][endy] = 100
	
	print(envment)
	print()
				
	print("width: "+str(width))
	print("height: "+str(height))
	print("startx: "+str(startx))
	print("starty: "+str(starty))
	print("endx: "+str(endx))
	print("endy: "+str(endy))
	print("ldmine_num: "+str(ldmine_num))
	print("g: "+str(g))
	print()

	queue = []
	queue.append([endx,endy])
	
	iteration = 0
	remaining_coords = 1 #Counts how many coordinates are left to be checked for this iteration.
	nexti_remaining_coords = 0
	
	while(len(queue)!=0): #When the queue is empty, convergence has been reached.
		
		current_coord = queue.pop(0)
		remaining_coords -= 1
		
		#Check if it's a terminal state, just add it's neighbours if it is a terminal state.
		if(envment[current_coord[0]][current_coord[1]] != 100):
			print('true')
			#For now, set it to a 100.
			envment[current_coord[0]][current_coord[1]] = 100
		
		if(validcoord([current_coord[0],current_coord[1]+1], width, height)): #down
			if(envment[current_coord[0]][current_coord[1]+1] != 100):
				queue.append([current_coord[0],current_coord[1]+1])
				nexti_remaining_coords += 1
				
		if(validcoord([current_coord[0],current_coord[1]-1], width, height)): #up
			if(envment[current_coord[0]][current_coord[1]-1] != 100):
				queue.append([current_coord[0],current_coord[1]-1])
				nexti_remaining_coords += 1
				
		if(validcoord([current_coord[0]-1,current_coord[1]], width, height)): #left
			if(envment[current_coord[0]-1][current_coord[1]] != 100):
				queue.append([current_coord[0]-1,current_coord[1]])
				nexti_remaining_coords += 1
				
		if(validcoord([current_coord[0],current_coord[1]+1], width, height)): #right
			if(envment[current_coord[0]][current_coord[1]+1] != 100):
				queue.append([current_coord[0],current_coord[1]+1])
				nexti_remaining_coords += 1
				
		if(remaining_coords == 0):
			remaining_coords = nexti_remaining_coords
			nexti_remaining_coords = 0
			#Export environment states to records.
	
	print(envment)
		
def validcoord(coord, width, height):
	if(coord[0]>width):
		return False
		
	if(coord[1]>height):
		return False
	
	if(coord[0]<0):
		return False
	
	if(coord[1]<0):
		return False

	return True
	
		
if __name__ == "__main__":
	main()
