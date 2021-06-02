import sys
import pprint
import matplotlib.pyplot as plt
from Animate import generateAnimat
import copy
import numpy as np
import random

def main():
	print("Welcome to QLearning")
	if(len(sys.argv)<3):
		print("Please specify environment dimensions. QLearning.py width height")
		system.exit(0)
		
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	
	startx = 0
	starty = 0
	
	endx = 1
	endy = 1
	
	ldmine_num = 1
	
	g = 0.5 #discount factor.
	n = 0.3
	e = 50
	
	epsilon = 0.8 #determines whether the agent favours exploration or exploitation.
	
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
				if(ldmine_num>((width*height)-2)):
					print("Not enough space for mines, pick a different number of mines.")
					system.exit(0)
				
			if(sys.argv[i] == "-gamma"):
				g = float(sys.argv[i+1]) 
			
			if(sys.argv[i] == "-learning"):
				n = float(sys.argv[i+1])
				
			if(sys.argv[i] == "-epochs"):
				e = float(sys.argv[i+1])
				
	envment=[[0]*width for _ in range (height)] #(0,0) is the top left corner.
	rewards=[[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)] # 3D Array, All set to 0.
	#element [..][..][1] stands for UP
	#element [..][..][0] stands for LEFT
	#element [..][..][3] stands for RIGHT
	#element [..][..][2] stands for DOWN
	
	
	print()
	coord = [endy,endx]
	
	#Set up rewards:
	if(validcoord([coord[0],coord[1]+1], width, height)): #right
		rewards[coord[0]][coord[1]+1][0] = 100 #The reward to move from the right neighbour to the left(end state) is 100.
					
	if(validcoord([coord[0],coord[1]-1], width, height)): #left
		rewards[coord[0]][coord[1]-1][3] = 100
					
	if(validcoord([coord[0]-1,coord[1]], width, height)): #up
		rewards[coord[0]-1][coord[1]][2] = 100
					
	if(validcoord([coord[0]+1,coord[1]], width, height)): #down
		rewards[coord[0]+1][coord[1]][1] = 100
	
	#pprint.pprint(rewards)
	
	envment[endy][endx] = 100
	to_place = ldmine_num
	
	while(to_place!=0):
		y = random.randint(0, height-1) 
		x =	random.randint(0, width-1)
		
		if(endy == y and endx == x): #Cannot place a mine on the terminal state.
			continue			
		elif(starty == y and startx == x):
			continue
			
		if(envment[y][x]!= -50):
			envment[y][x] = -50
			
		to_place-=1
	
	print("width: "+str(width))
	print("height: "+str(height))
	print("startx: "+str(startx))
	print("starty: "+str(starty))
	print("endx: "+str(endx))
	print("endy: "+str(endy))
	print("ldmine_num: "+str(ldmine_num))
	print("g: "+str(g))
	print()
	
	#Begin Q-Learning.
	queue = []
	records = []
	
	xintrvls = (int)((width-1)/e)
	yintrvls = (int)((height-1)/e)
	epsintrvls = (epsilon/2)/e
	episodes = 0
	epconstrain = int((80/100) * e)
	
	xlower = 0
	xupper = width-1
	
	ylower = 0
	yupper = height -1
	
	print("Begin Learning")
	while(e>0):
		#Slowly constrain the starting point from a random state to the initial starting point.
		xr = random.randint(xlower, xupper)
		yr = random.randint(ylower, yupper)
		
		queue.append([yr,xr]) #y x
		
		
		while(True):
			start_coord = queue.pop(0)

			if(start_coord[0] == endy and start_coord[1] == endx): #if end or mine, break.
				break
			elif(envment[start_coord[0]][start_coord[1]] == -50):
				break
				
			valuelist = []
			paths = []
			#Find Possible actions to take.
			if(validcoord([start_coord[0],start_coord[1]+1], width, height)):
				valuelist.append(envment[start_coord[0]][start_coord[1]+1])
				paths.append(3) #right
				
			if(validcoord([start_coord[0],start_coord[1]-1], width, height)):
				valuelist.append(envment[start_coord[0]][start_coord[1]-1])
				paths.append(0) #left
			
			if(validcoord([start_coord[0]-1,start_coord[1]], width, height)):
				valuelist.append(envment[start_coord[0]-1][start_coord[1]])
				paths.append(1) #up
				
			if(validcoord([start_coord[0]+1,start_coord[1]], width, height)):
				valuelist.append(envment[start_coord[0]+1][start_coord[1]])
				paths.append(2) #down
			
			
			direction = 0
			ind = np.argmax(valuelist)
			best = np.amax(valuelist)
		
			found = np.where(valuelist == best)[0]	
		
			if(len(found)>1): #Multiple similar Q values.
				direction = paths[found[random.randint(0,len(found)-1)]]
			else:
				direction = paths[ind]
				
			if((random.uniform(0,1)) < epsilon): #Explore, else Exploit.
				ind = random.randint(0, len(valuelist)-1)
				direction = paths[ind]
				
			next_coord = []
			
			
			#Pick an action depending on epsilon.
			if(direction == 3 ):#right
				next_coord = [start_coord[0],start_coord[1]+1]
				
			if(direction == 0 ):#left
				next_coord = [start_coord[0],start_coord[1]-1]
				
			if(direction == 1 ):#up
				next_coord = [start_coord[0]-1,start_coord[1]]
				
			if(direction == 2 ):#down
				next_coord = [start_coord[0]+1,start_coord[1]]
				
			#Check Q Values of NextCoordinate.
			
			valuelist.clear()
			
			if(validcoord([next_coord[0],next_coord[1]+1], width, height)):
				valuelist.append(envment[next_coord[0]][next_coord[1]+1])
				
			if(validcoord([next_coord[0],next_coord[1]-1], width, height)):
				valuelist.append(envment[next_coord[0]][next_coord[1]-1])
				
			if(validcoord([next_coord[0]-1,next_coord[1]], width, height)):
				valuelist.append(envment[next_coord[0]-1][next_coord[1]])
				
			if(validcoord([next_coord[0]+1,next_coord[1]], width, height)):
				valuelist.append(envment[next_coord[0]+1][next_coord[1]])
			
			envment[start_coord[0]][start_coord[1]] += action_value(n,rewards[start_coord[0]][start_coord[1]][direction], g, valuelist, envment[start_coord[0]][start_coord[1]])

			queue.append(next_coord)
		
		#Constrain the starting point.
		if(episodes>epconstrain):
			if(xlower!=startx):
				xlower+=1
			if(xupper!=startx):
				xupper-=1
			if(ylower!=starty):
				ylower+=1
			if(yupper!=starty):
				yupper-=1
			
		e-=1 #Go to next Episode.
		episodes += 1
		epsilon -= epsintrvls
		records.append(copy.deepcopy(envment))
	print("Learning Complete")
	#Get optimal policy.
	
	start_coord = [starty,startx]
	opt_pol = []
	
	print("Obtaining Optimal Policy")
	while(True):
		opt_pol.append((start_coord[1],start_coord[0]))
		
		if(start_coord[0]== endy and start_coord[1] == endx):
			break
			
		paths = []	
		
		#print(envment[start_coord[0]][start_coord[1]+1],envment[start_coord[0]][start_coord[1]-1],envment[start_coord[0]-1][start_coord[1]],envment[start_coord[0]+1][start_coord[1]])
		valuelist = []
		
		if(validcoord([start_coord[0],start_coord[1]+1], width, height)):
			if(envment[start_coord[0]][start_coord[1]+1]!=-50):
				valuelist.append(envment[start_coord[0]][start_coord[1]+1])
				paths.append(3) #right
			
		if(validcoord([start_coord[0],start_coord[1]-1], width, height)):
			if(envment[start_coord[0]][start_coord[1]-1]!=-50):
				valuelist.append(envment[start_coord[0]][start_coord[1]-1])
				paths.append(0) #left
				
		if(validcoord([start_coord[0]-1,start_coord[1]], width, height)):
			if(envment[start_coord[0]-1][start_coord[1]]!=-50):
				valuelist.append(envment[start_coord[0]-1][start_coord[1]])
				paths.append(1) #up
			
		if(validcoord([start_coord[0]+1,start_coord[1]], width, height)):
			if(envment[start_coord[0]+1][start_coord[1]]!=-50):
				valuelist.append(envment[start_coord[0]+1][start_coord[1]])
				paths.append(2) #down
				
				
		direction = 0
		if(len(valuelist)<1):
			print("point is surrounded by mines. Please retry, Quitting...")
			System.exit(0)
			
		best = np.amax(valuelist)
		ind = np.argmax(valuelist)
		
		found = np.where(valuelist == best)[0]	
		
		if(len(found)>1): #Multiple similar Q values.
			direction = paths[found[random.randint(0,len(found)-1)]]
		else:
			direction = paths[ind]
	
			#Pick an action depending on epsilon. If some states have the same Q value, the agent may traverse to a different state from the one picked but that is okay since it will still be picking the best state or a random state.
		if(direction == 3 ):#right
			start_coord = [start_coord[0],start_coord[1]+1]
			continue
				
		if(direction == 0 ):#left
			start_coord = [start_coord[0],start_coord[1]-1]
			continue
				
		if(direction == 1 ):#up
			start_coord = [start_coord[0]-1,start_coord[1]]
			continue
				
		if(direction == 2 ):#down
			start_coord = [start_coord[0]+1,start_coord[1]]
			continue
	
	#Produce animation.
	print("Creating Animation")
	start_state = (startx, starty)
	end_state = (endx, endy)
	
	mines = []
	
	anim, fig, ax = generateAnimat(records, start_state, end_state, mines=mines, opt_pol=opt_pol, 
		start_val=-10, end_val=100, mine_val=150, just_vals=False, generate_gif=False,
		vmin = -10, vmax = 150)

	plt.show()
def action_value(n,reward, discount, value, this_val):
	return n*(reward + (discount * (np.amax(value) - this_val)))
			
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
