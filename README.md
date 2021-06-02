#How to Run
In the terminal, type 'make' to  automatically create a virtual environment and install required packages.

'make clean' to remove binary files.

to run, type the following:

```bash
	python3 ValueIteration.py width height -start x y -end x y -k mines -gamma y
```
where:
x and y are int coordinates of starting or end points.
mines is the number of mines
y is the discount rate.

```bash
	python3 QLearning.py 10 10 width height -start x y -end x y -k mines -gamma y -learning n -epochs e
```
where:
n is the learning rate
e is the episodes/epochs

#FILES
ValueIteration.py implements the Value iterative method of reinforcement learning and generates values for all the states.

QLearning.py performs the other type of reinforcement learning. Note: The end point starts with a Q value of 100 and the rewards to get to this state are also 100.

Animate.py is required to generate animations of how the Agent advances in the environment using value iteration or q learning.

requirements.txt lists the required packages to be installed.

.gitignore excludes binary files from the repository.

