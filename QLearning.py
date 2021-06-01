import sys
import pprint
import matplotlib.pyplot as plt
from Animate import generateAnimat
import copy
import random

def main():
	print("Welcome")
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
	e = 5
	
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
				
			if(sys.argv[i] == "-epochs");
				e = float(sys.argv[i+1])
