install: venv 
		. venv/bin/activate; pip3 install -Ur requirements.txt
venv :
	test -d venv || python3 -m venv venv
 
clean:
	rm -rf venv
	find -iname "*.pyc" -delete
 
run:
	@python3 ValueIteration.py 3 2 -start 0 0 -end 2 0 -k 3

run_test:
	@python3 ValueIteration.py 10 10 -start 2 3 -end 4 5 -k 7 -gamma 0.5

run1:
	@python3 QLearning.py 3 2 -start 0 0 -end 2 0 -k 3 -gamma 0.5 -learning 0.5 -epochs 50
run_c:
	@python3 ValueIteration.py 10 10 -start 0 0 -end 9 9 -k 0 -gamma 0.5
	
run_c2:
	@python3 ValueIteration.py 10 10 -start 0 0 -end 9 9 -k 20 -gamma 0.5
	
runq:
	@python3 QLearning.py 15 15 -start 1 4 -end 14 14 -k 35 -gamma 0.5 -learning 0.99 -epochs 50

runq2:
	@python3 QLearning.py 10 10 -start 2 3 -end 4 5 -k 7 -gamma 0.7 -learning 0.3 -epochs 100

runq3:
	@python3 QLearning.py 10 10 -start 0 0 -end 9 9 -k 7 -gamma 0.5 -learning 0.3 -epochs 100
	
example:
	@python3 Example.py
	
	#source ./venv/bin/activate
