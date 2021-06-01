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

runq:
	@python3
example:
	@python3 Example.py
	
	#source ./venv/bin/activate
