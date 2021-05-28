import sys

def main():
	print("Welcome")
	if(len(sys.argv)<3):
		print("Please specify environment dimensions. ValueIteration.py width height")
		
		
	width = sys.argv[1]
	height = sys.argv[2]
	
	startx = "0"
	starty = "0"
	
	endx = "1"
	endy = "1"
	
	ldmine_num = "1"
	
	g = "0.5" #discount factor.
	
	if(len(sys.argv)>3):
		for i in range(3,len(sys.argv)):
			if(sys.argv[i] == "-start"):
				startx = sys.argv[i+1]
				starty = sys.argv[i+2]
			
			if(sys.argv[i] == "-end"):
				endx = sys.argv[i+1]
				endy = sys.argv[i+2]
				
			if(sys.argv[i] == "-k"):
				ldmine_num = sys.argv[i+1]
				
			if(sys.argv[i] == "-gamma"):
				g = sys.argv[i+1] 
				
	print("width: "+width)
	print("height: "+height)
	print("startx: "+startx)
	print("starty: "+starty)
	print("endx: "+endx)
	print("endy: "+endy)
	print("ldmine_num: "+ldmine_num)
	print("g: "+g)


if __name__ == "__main__":
	main()
