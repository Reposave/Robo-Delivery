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
				
				
	record=[[0]*width for _ in range (height)]
	rewards=[[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)] #All set to 0.
	
	pprint.pprint(rewards)
	print()
	
	record[endx][endy] = 100
	
	print(record)
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

if __name__ == "__main__":
	main()
