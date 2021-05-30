install: venv 
		. venv/bin/activate; pip3 install -Ur requirements.txt
venv :
	test -d venv || python3 -m venv venv
 
clean:
	rm -rf venv
	find -iname "*.pyc" -delete
 
run:
	@python3 ValueIteration.py 3 2

run_test:
	@python3 ValueIteration.py 10 10 -start 2 3 -end 4 5 -k 2 -gamma 0.4
	
example:
	@python3 Example.py
