# Reinforcement Learning in Python
Implementing Reinforcement Learning Algorithms for global path planning of mobile robot

### Reference to:
[1] Valentyn N Sichkar. Reinforcement Learning Algorithms for global path planning // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python (date of access: XX.XX.XXXX)

## Description
RL Algorithms implemented in Python for the task of global path planning for mobile robot.
<br/>Experimental results with different Environments.
<br/>Code is supported with a lot of comments. It will guide you step by step through entire idea of implementation.
<br/>
<br/>Each example consists of three files:
<br/>env.py - building an environment with obstacles.
<br/>agent_brain.py - implementation of algorithm itself.
<br/>run_agent.py - running the experiments.

## Content
* [RL_Q-Learning_E-1](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Q-Learning_E1)
* [RL_Q-Learning_E-2](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Q-Learning_E2)
* [RL_Q-Learning_E-3](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Q-Learning_E3)
* [RL_Sarsa_E-1](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Sarsa_E1)
* [RL_Sarsa_E-2](https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python/tree/master/RL_Sarsa_E2)

<br/>

### RL Q-Learning Environment-1. Experimental results
#### Environment-1 with mobile robot, goal and obstacles
<img src="images/Environment-1.gif" alt="RL_Q-Learning_E-1" width=362 height=391> <img src="images/Environment-1.png" alt="RL_Q-Learning_E-1" width=362 height=391>


#### Q-learning algorithm resulted chart for the environment-1 represents number of episodes via number of steps and number of episodes via cost for each episode
![RL_Q-Learning_C-1](images/Charts-1.png)

#### Final Q-table with values from the final shortest route for environment-1
![RL_Q-Learning_T-1](images/Q-Table-E-1.png)
<br/>Looking at the values of the table we can see the decision for the next action made by agent (mobile robot). The sequence of final actions to reach the goal after the Q-table is filled with knowledge is the following: *down-right-down-down-down-right-down-right-down-right-down-down-right-right-up-up.*
<br/>During the experiment with Q-learning algorithm the found shortest route to reach the goal for the environment-1 consist of 16 steps and the found longest rout to reach the goal consists of 185 steps.

<br/>

### RL Q-Learning Environment-2. Experimental results
#### Bigger environment-2 with more obstacles
![RL_Q-Learning_E-2](images/Environment-2.png)

#### Q-learning algorithm resulted chart for the environment-2 represents number of episodes via number of steps and number of episodes via cost for each episode
![RL_Q-Learning_C-2](images/Charts-2.png)

#### Final Q-table with values from the final shortest route for environment-1
![RL_Q-Learning_T-2](images/Q-Table-E-2.png)

<br/>

### RL Q-Learning Environment-3. Experimental results
#### Super complex environment-3 with a lot of obstacles
![RL_Q-Learning_E-3](images/Environment-3.png)


## MIT License
## Copyright (c) 2018 Valentyn N Sichkar
## github.com/sichkar-valentyn
### Reference to:
[1] Valentyn N Sichkar. Reinforcement Learning Algorithms for global path planning // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Reinforcement_Learning_in_Python (date of access: XX.XX.XXXX)
