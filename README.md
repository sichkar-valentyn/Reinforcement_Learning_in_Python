# Reinforcement Learning in Python
Implementing Reinforcement Learning Algorithms for global path planning of mobile robot

### Reference to:
[1] Valentyn N Sichkar. Reinforcement Learning Algorithms for global path planning // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python (date of access: XX.XX.XXXX)

## Description
RL Algorithms implemented in Python for the task of global path planning for mobile robot.
Experimental results with different Environments.

## Content
* [RL_Q-Learning_E-1](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Q-Learning_E1)
* [RL_Q-Learning_E-2](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Q-Learning_E2)
* [RL_Q-Learning_E-3](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Q-Learning_E3)

### RL Q-Learning Environment-1. Experimental results
<b>Environment-1 with mobile robot, goal and obstacles</b>
![RL_Q-Learning_E-1](images/Environment-1.png)
<br/><b>Q-learning algorithm resulted chart for the environment-1 represents number of episodes via number of steps and number of episodes via cost for each episode</b>
![RL_Q-Learning_C-1](images/Charts-1.png)
<br/><b>Final Q-table with values from the final shortest route for environment-1</b>
![RL_Q-Learning_T-1](images/Q-Table-E-1.png)
<br/>Looking at the values of the table we can see the decision for the next action made by agent (mobile robot). The sequence of final actions to reach the goal after the Q-table is filled with knowledge is the following: *down-right-down-down-down-right-down-right-down-right-down-down-right-right-up-up.*
<br/>During the experiment with Q-learning algorithm the found shortest route to reach the goal for the environment-1 consist of 16 steps and the found longest rout to reach the goal consists of 185 steps.


### RL Q-Learning Environment-2. Experimental results
![RL_Q-Learning_E-2](images/Environment-2.png)
![RL_Q-Learning_C-2](images/Charts-2.png)

### RL Q-Learning Environment-3. Experimental results
![RL_Q-Learning_E-3](images/Environment-3.png)
![RL_Q-Learning_c-3](images/Charts-3.png)

## MIT License
## Copyright (c) 2018 Valentyn N Sichkar
## github.com/sichkar-valentyn
### Reference to:
[1] Valentyn N Sichkar. Reinforcement Learning Algorithms for global path planning // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python (date of access: XX.XX.XXXX)
