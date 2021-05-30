import sys
import pprint
import matplotlib.pyplot as plt
from Animate import generateAnimat
import copy

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
				
				
	envment=[[0]*width for _ in range (height)] #(0,0) is the top left corner.
	rewards=[[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)] # 3D Array, All set to 0.
	#element [..][..][0] stands for UP
	#element [..][..][1] stands for LEFT
	#element [..][..][2] stands for RIGHT
	#element [..][..][3] stands for DOWN
	
	pprint.pprint(rewards)
	print()
	
	envment[endy][endx] = 100
	
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
	queue.append([endy,endx]) #y x
	
	iteration = 0
	remaining_coords = 1 #Counts how many coordinates are left to be checked for this iteration.
	nexti_remaining_coords = 0
	
	record = []
	
	while(len(queue)!=0): #When the queue is empty, convergence has been reached.
		
		current_coord = queue.pop(0)
		remaining_coords -= 1
		
		prev_value = envment[current_coord[0]][current_coord[1]]
		
		#Check if it's a terminal state, just add it's neighbours if it is a terminal state.
		if(envment[current_coord[0]][current_coord[1]] != 100):
			results = []
			
			Reward = 0
			Value = 0
			
			if(validcoord([current_coord[0],current_coord[1]+1], width, height)): #right
					Reward = rewards[current_coord[0]][current_coord[1]+1][3]
					Value = envment[current_coord[0]][current_coord[1]+1]
					
					results.append(action_value(Reward,g,Value))
					
			if(validcoord([current_coord[0],current_coord[1]-1], width, height)): #left
					Reward = rewards[current_coord[0]][current_coord[1]-1][0]
					Value = envment[current_coord[0]][current_coord[1]-1]
					
					results.append(action_value(Reward,g,Value))
					
			if(validcoord([current_coord[0]-1,current_coord[1]], width, height)): #up
					Reward = rewards[current_coord[0]-1][current_coord[1]][1]
					Value = envment[current_coord[0]-1][current_coord[1]]
					
					results.append(action_value(Reward,g,Value))
					
			if(validcoord([current_coord[0]+1,current_coord[1]], width, height)): #down
					Reward = rewards[current_coord[0]+1][current_coord[1]][2]
					Value = envment[current_coord[0]+1][current_coord[1]]
					
					results.append(action_value(Reward,g,Value))
					
			envment[current_coord[0]][current_coord[1]] = max(results)
					
		if(prev_value != envment[current_coord[0]][current_coord[1]] or envment[current_coord[0]][current_coord[1]] == 100): #If the value of the current state changed or we have just started, the neighbours may have to be updated as well.
		
			if(validcoord([current_coord[0],current_coord[1]+1], width, height)): #right
				if(envment[current_coord[0]][current_coord[1]+1] != 100):
					queue.append([current_coord[0],current_coord[1]+1])
					nexti_remaining_coords += 1
					
			if(validcoord([current_coord[0],current_coord[1]-1], width, height)): #left
				if(envment[current_coord[0]][current_coord[1]-1] != 100):
					queue.append([current_coord[0],current_coord[1]-1])
					nexti_remaining_coords += 1
					
			if(validcoord([current_coord[0]-1,current_coord[1]], width, height)): #up
				if(envment[current_coord[0]-1][current_coord[1]] != 100):
					queue.append([current_coord[0]-1,current_coord[1]])
					nexti_remaining_coords += 1
					
			if(validcoord([current_coord[0]+1,current_coord[1]], width, height)): #down
				if(envment[current_coord[0]+1][current_coord[1]] != 100):
					queue.append([current_coord[0]+1,current_coord[1]])
					nexti_remaining_coords += 1
				
		if(remaining_coords == 0):
			remaining_coords = nexti_remaining_coords
			nexti_remaining_coords = 0
			#Export environment states to records.
			record.append([envment])
	
	#Get optimal policy.
	
	start_coord = [starty,startx]
	opt_pol = []
	
	
	while(True):
	
		print(start_coord)
		opt_pol.append(start_coord)
		
		if(start_coord[0]== endy and start_coord[1] == endx):
			break
			
		#print(envment[start_coord[0]][start_coord[1]+1],envment[start_coord[0]][start_coord[1]-1],envment[start_coord[0]-1][start_coord[1]],envment[start_coord[0]+1][start_coord[1]])
		valuelist = []
		
		if(validcoord([start_coord[0],start_coord[1]+1], width, height)):
			valuelist.append(envment[start_coord[0]][start_coord[1]+1])
			
		if(validcoord([start_coord[0],start_coord[1]-1], width, height)):
			valuelist.append(envment[start_coord[0]][start_coord[1]-1])
			
		if(validcoord([start_coord[0]-1,start_coord[1]], width, height)):
			valuelist.append(envment[start_coord[0]-1][start_coord[1]])
			
		if(validcoord([start_coord[0]+1,start_coord[1]], width, height)):
			valuelist.append(envment[start_coord[0]+1][start_coord[1]])
				
		best = max(valuelist)
		
		if(validcoord([start_coord[0],start_coord[1]+1], width, height)):
			if(best == envment[start_coord[0]][start_coord[1]+1]):
				start_coord = [start_coord[0],start_coord[1]+1]
				continue
		
		if(validcoord([start_coord[0],start_coord[1]-1], width, height)):
			if(best == envment[start_coord[0]][start_coord[1]-1]):
				start_coord = [start_coord[0],start_coord[1]-1]
				continue
		
		if(validcoord([start_coord[0]-1,start_coord[1]], width, height)):
			if(best == envment[start_coord[0]-1][start_coord[1]]):
				start_coord = [start_coord[0]-1,start_coord[1]]
				continue
		
		if(validcoord([start_coord[0]+1,start_coord[1]], width, height)):
			if(best == envment[start_coord[0]+1][start_coord[1]]):
				start_coord = [start_coord[0]+1,start_coord[1]]
				continue
		
	print(opt_pol)
	print(envment)
	print(record)
	
	#Produce animation.
	start_state = (starty, startx)
	end_state = (endy, endx)
	
	mines = []

def action_value(reward, discount, value):
	return reward + (discount * value)
			
def validcoord(coord, width, height):
	#print(coord)
	if(coord[0]>height-1):
		return False
		
	if(coord[1]>width-1):
		return False
	
	if(coord[0]<0):
		return False
	
	if(coord[1]<0):
		return False

	return True
	
		
if __name__ == "__main__":
	main()
