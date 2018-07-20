# File: env.py
# Description: Building the environment-3 for the Mobile Robot to explore
# Agent - Mobile Robot
# Obstacles - 'road closed', 'trees', 'traffic lights', 'buildings'
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# Valentyn N Sichkar. Reinforcement Learning Algorithms for global path planning // GitHub platform. DOI: 10.5281/zenodo.1317899



# Importing libraries
import numpy as np  # To deal with data in form of matrices
import tkinter as tk  # To build GUI
import time  # Time is needed to slow down the agent and to see how he runs
from PIL import Image, ImageTk  # For adding images into the canvas widget

# Setting the sizes for the environment
pixels = 20   # pixels
env_height = 30  # grid height
env_width = 30  # grid width

# Global variable for dictionary with coordinates for the final route
a = {}


# Creating class for the environment
class Environment(tk.Tk, object):
    def __init__(self):
        super(Environment, self).__init__()
        self.action_space = ['up', 'down', 'left', 'right']
        self.n_actions = len(self.action_space)
        self.title('RL Q-learning. Sichkar Valentyn')
        self.geometry('{0}x{1}'.format(env_height * pixels, env_height * pixels))
        self.build_environment()

        # Dictionaries to draw the final route
        self.d = {}
        self.f = {}

        # Key for the dictionaries
        self.i = 0

        # Writing the final dictionary first time
        self.c = True

        # Showing the steps for longest found route
        self.longest = 0

        # Showing the steps for the shortest route
        self.shortest = 0

    # Function to build the environment
    def build_environment(self):
        self.canvas_widget = tk.Canvas(self,  bg='white',
                                       height=env_height * pixels,
                                       width=env_width * pixels)

        # Uploading an image for background
        img_background = Image.open("images/bg.png")
        self.background = ImageTk.PhotoImage(img_background)
        # Creating background on the widget
        self.bg = self.canvas_widget.create_image(0, 0, anchor='nw', image=self.background)

        # Creating grid lines
        for column in range(0, env_width * pixels, pixels):
            x0, y0, x1, y1 = column, 0, column, env_height * pixels
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')
        for row in range(0, env_height * pixels, pixels):
            x0, y0, x1, y1 = 0, row, env_height * pixels, row
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

        # Creating objects of  Obstacles
        # An array to help with building rectangles
        self.o = np.array([pixels / 2, pixels / 2])

        # Obstacle 1
        # Defining the center of obstacle 1
        obstacle1_center = self.o + np.array([pixels, pixels * 2])
        # Building the obstacle 1
        self.obstacle1 = self.canvas_widget.create_rectangle(
            obstacle1_center[0] - 10, obstacle1_center[1] - 10,  # Top left corner
            obstacle1_center[0] + 10, obstacle1_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 1 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle1 = [self.canvas_widget.coords(self.obstacle1)[0] + 3,
         self.canvas_widget.coords(self.obstacle1)[1] + 3,
         self.canvas_widget.coords(self.obstacle1)[2] - 3,
         self.canvas_widget.coords(self.obstacle1)[3] - 3]

        # Obstacle 2
        # Defining the center of obstacle 2
        obstacle2_center = self.o + np.array([pixels * 2, pixels * 2])
        # Building the obstacle 2
        self.obstacle2 = self.canvas_widget.create_rectangle(
            obstacle2_center[0] - 10, obstacle2_center[1] - 10,  # Top left corner
            obstacle2_center[0] + 10, obstacle2_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 2 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle2 = [self.canvas_widget.coords(self.obstacle2)[0] + 3,
         self.canvas_widget.coords(self.obstacle2)[1] + 3,
         self.canvas_widget.coords(self.obstacle2)[2] - 3,
         self.canvas_widget.coords(self.obstacle2)[3] - 3]

        # Obstacle 3
        # Defining the center of obstacle 3
        obstacle3_center = self.o + np.array([pixels * 3, pixels * 2])
        # Building the obstacle 3
        self.obstacle3 = self.canvas_widget.create_rectangle(
            obstacle3_center[0] - 10, obstacle3_center[1] - 10,  # Top left corner
            obstacle3_center[0] + 10, obstacle3_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 3 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle3 = [self.canvas_widget.coords(self.obstacle3)[0] + 3,
         self.canvas_widget.coords(self.obstacle3)[1] + 3,
         self.canvas_widget.coords(self.obstacle3)[2] - 3,
         self.canvas_widget.coords(self.obstacle3)[3] - 3]

        # Obstacle 4
        # Defining the center of obstacle 4
        obstacle4_center = self.o + np.array([pixels * 3, pixels * 3])
        # Building the obstacle 4
        self.obstacle4 = self.canvas_widget.create_rectangle(
            obstacle4_center[0] - 10, obstacle4_center[1] - 10,  # Top left corner
            obstacle4_center[0] + 10, obstacle4_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 4 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle4 = [self.canvas_widget.coords(self.obstacle4)[0] + 3,
         self.canvas_widget.coords(self.obstacle4)[1] + 3,
         self.canvas_widget.coords(self.obstacle4)[2] - 3,
         self.canvas_widget.coords(self.obstacle4)[3] - 3]

        # Obstacle 5
        # Defining the center of obstacle 5
        obstacle5_center = self.o + np.array([pixels * 23, pixels])
        # Building the obstacle 5
        self.obstacle5 = self.canvas_widget.create_rectangle(
            obstacle5_center[0] - 10, obstacle5_center[1] - 10,  # Top left corner
            obstacle5_center[0] + 10, obstacle5_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 2 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle5 = [self.canvas_widget.coords(self.obstacle5)[0] + 3,
         self.canvas_widget.coords(self.obstacle5)[1] + 3,
         self.canvas_widget.coords(self.obstacle5)[2] - 3,
         self.canvas_widget.coords(self.obstacle5)[3] - 3]

        # Obstacle 6
        # Defining the center of obstacle 6
        obstacle6_center = self.o + np.array([pixels * 6, pixels])
        # Building the obstacle 6
        self.obstacle6 = self.canvas_widget.create_rectangle(
            obstacle6_center[0] - 10, obstacle6_center[1] - 10,  # Top left corner
            obstacle6_center[0] + 10, obstacle6_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 6 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle6 = [self.canvas_widget.coords(self.obstacle6)[0] + 3,
         self.canvas_widget.coords(self.obstacle6)[1] + 3,
         self.canvas_widget.coords(self.obstacle6)[2] - 3,
         self.canvas_widget.coords(self.obstacle6)[3] - 3]

        # Obstacle 7
        # Defining the center of obstacle 7
        obstacle7_center = self.o + np.array([pixels * 6, pixels * 2])
        # Building the obstacle 7
        self.obstacle7 = self.canvas_widget.create_rectangle(
            obstacle7_center[0] - 10, obstacle7_center[1] - 10,  # Top left corner
            obstacle7_center[0] + 10, obstacle7_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 7 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle7 = [self.canvas_widget.coords(self.obstacle7)[0] + 3,
         self.canvas_widget.coords(self.obstacle7)[1] + 3,
         self.canvas_widget.coords(self.obstacle7)[2] - 3,
         self.canvas_widget.coords(self.obstacle7)[3] - 3]

        # Obstacle 8
        # Defining the center of obstacle 8
        obstacle8_center = self.o + np.array([pixels * 7, pixels * 2])
        # Building the obstacle 8
        self.obstacle8 = self.canvas_widget.create_rectangle(
            obstacle8_center[0] - 10, obstacle8_center[1] - 10,  # Top left corner
            obstacle8_center[0] + 10, obstacle8_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 8 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle8 = [self.canvas_widget.coords(self.obstacle8)[0] + 3,
         self.canvas_widget.coords(self.obstacle8)[1] + 3,
         self.canvas_widget.coords(self.obstacle8)[2] - 3,
         self.canvas_widget.coords(self.obstacle8)[3] - 3]

        # Obstacle 9
        # Defining the center of obstacle 9
        obstacle9_center = self.o + np.array([pixels * 8, pixels * 2])
        # Building the obstacle 9
        self.obstacle9 = self.canvas_widget.create_rectangle(
            obstacle9_center[0] - 10, obstacle9_center[1] - 10,  # Top left corner
            obstacle9_center[0] + 10, obstacle9_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 9 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle9 = [self.canvas_widget.coords(self.obstacle9)[0] + 3,
         self.canvas_widget.coords(self.obstacle9)[1] + 3,
         self.canvas_widget.coords(self.obstacle9)[2] - 3,
         self.canvas_widget.coords(self.obstacle9)[3] - 3]

        # Obstacle 10
        # Defining the center of obstacle 10
        obstacle10_center = self.o + np.array([pixels * 10, pixels * 4])
        # Building the obstacle 10
        self.obstacle10 = self.canvas_widget.create_rectangle(
            obstacle10_center[0] - 10, obstacle10_center[1] - 10,  # Top left corner
            obstacle10_center[0] + 10, obstacle10_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 10 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle10 = [self.canvas_widget.coords(self.obstacle10)[0] + 3,
         self.canvas_widget.coords(self.obstacle10)[1] + 3,
         self.canvas_widget.coords(self.obstacle10)[2] - 3,
         self.canvas_widget.coords(self.obstacle10)[3] - 3]

        # Obstacle 11
        # Defining the center of obstacle 11
        obstacle11_center = self.o + np.array([pixels * 10, pixels * 5])
        # Building the obstacle 11
        self.obstacle11 = self.canvas_widget.create_rectangle(
            obstacle11_center[0] - 10, obstacle11_center[1] - 10,  # Top left corner
            obstacle11_center[0] + 10, obstacle11_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 11 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle11 = [self.canvas_widget.coords(self.obstacle11)[0] + 3,
         self.canvas_widget.coords(self.obstacle11)[1] + 3,
         self.canvas_widget.coords(self.obstacle11)[2] - 3,
         self.canvas_widget.coords(self.obstacle11)[3] - 3]

        # Obstacle 12
        # Defining the center of obstacle 12
        obstacle12_center = self.o + np.array([pixels * 10, pixels * 6])
        # Building the obstacle 12
        self.obstacle12 = self.canvas_widget.create_rectangle(
            obstacle12_center[0] - 10, obstacle12_center[1] - 10,  # Top left corner
            obstacle12_center[0] + 10, obstacle12_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 12 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle12 = [self.canvas_widget.coords(self.obstacle12)[0] + 3,
         self.canvas_widget.coords(self.obstacle12)[1] + 3,
         self.canvas_widget.coords(self.obstacle12)[2] - 3,
         self.canvas_widget.coords(self.obstacle12)[3] - 3]

        # Obstacle 13
        # Defining the center of obstacle 13
        obstacle13_center = self.o + np.array([pixels * 11, pixels * 5])
        # Building the obstacle 13
        self.obstacle13 = self.canvas_widget.create_rectangle(
            obstacle13_center[0] - 10, obstacle13_center[1] - 10,  # Top left corner
            obstacle13_center[0] + 10, obstacle13_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 13 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle13 = [self.canvas_widget.coords(self.obstacle13)[0] + 3,
         self.canvas_widget.coords(self.obstacle13)[1] + 3,
         self.canvas_widget.coords(self.obstacle13)[2] - 3,
         self.canvas_widget.coords(self.obstacle13)[3] - 3]

        # Obstacle 14
        # Defining the center of obstacle 14
        obstacle14_center = self.o + np.array([pixels * 12, pixels * 5])
        # Building the obstacle 14
        self.obstacle14 = self.canvas_widget.create_rectangle(
            obstacle14_center[0] - 10, obstacle14_center[1] - 10,  # Top left corner
            obstacle14_center[0] + 10, obstacle14_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 14 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle14 = [self.canvas_widget.coords(self.obstacle14)[0] + 3,
         self.canvas_widget.coords(self.obstacle14)[1] + 3,
         self.canvas_widget.coords(self.obstacle14)[2] - 3,
         self.canvas_widget.coords(self.obstacle14)[3] - 3]

        # Obstacle 15
        # Defining the center of obstacle 15
        obstacle15_center = self.o + np.array([pixels * 13, pixels * 5])
        # Building the obstacle 15
        self.obstacle15 = self.canvas_widget.create_rectangle(
            obstacle15_center[0] - 10, obstacle15_center[1] - 10,  # Top left corner
            obstacle15_center[0] + 10, obstacle15_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 15 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle15 = [self.canvas_widget.coords(self.obstacle15)[0] + 3,
         self.canvas_widget.coords(self.obstacle15)[1] + 3,
         self.canvas_widget.coords(self.obstacle15)[2] - 3,
         self.canvas_widget.coords(self.obstacle15)[3] - 3]

        # Obstacle 16
        # Defining the center of obstacle 16
        obstacle16_center = self.o + np.array([pixels * 14, pixels * 5])
        # Building the obstacle 16
        self.obstacle16 = self.canvas_widget.create_rectangle(
            obstacle16_center[0] - 10, obstacle16_center[1] - 10,  # Top left corner
            obstacle16_center[0] + 10, obstacle16_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 16 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle16 = [self.canvas_widget.coords(self.obstacle16)[0] + 3,
         self.canvas_widget.coords(self.obstacle16)[1] + 3,
         self.canvas_widget.coords(self.obstacle16)[2] - 3,
         self.canvas_widget.coords(self.obstacle16)[3] - 3]

        # Obstacle 17
        # Defining the center of obstacle 17
        obstacle17_center = self.o + np.array([pixels * 15, pixels * 4])
        # Building the obstacle 17
        self.obstacle17 = self.canvas_widget.create_rectangle(
            obstacle17_center[0] - 10, obstacle17_center[1] - 10,  # Top left corner
            obstacle17_center[0] + 10, obstacle17_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 17 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle17 = [self.canvas_widget.coords(self.obstacle17)[0] + 3,
         self.canvas_widget.coords(self.obstacle17)[1] + 3,
         self.canvas_widget.coords(self.obstacle17)[2] - 3,
         self.canvas_widget.coords(self.obstacle17)[3] - 3]

        # Obstacle 18
        # Defining the center of obstacle 18
        obstacle18_center = self.o + np.array([pixels * 15, pixels * 5])
        # Building the obstacle 18
        self.obstacle18 = self.canvas_widget.create_rectangle(
            obstacle18_center[0] - 10, obstacle18_center[1] - 10,  # Top left corner
            obstacle18_center[0] + 10, obstacle18_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 18 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle18 = [self.canvas_widget.coords(self.obstacle18)[0] + 3,
         self.canvas_widget.coords(self.obstacle18)[1] + 3,
         self.canvas_widget.coords(self.obstacle18)[2] - 3,
         self.canvas_widget.coords(self.obstacle18)[3] - 3]

        # Obstacle 19
        # Defining the center of obstacle 19
        obstacle19_center = self.o + np.array([pixels * 15, pixels * 6])
        # Building the obstacle 19
        self.obstacle19 = self.canvas_widget.create_rectangle(
            obstacle19_center[0] - 10, obstacle19_center[1] - 10,  # Top left corner
            obstacle19_center[0] + 10, obstacle19_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 19 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle19 = [self.canvas_widget.coords(self.obstacle19)[0] + 3,
         self.canvas_widget.coords(self.obstacle19)[1] + 3,
         self.canvas_widget.coords(self.obstacle19)[2] - 3,
         self.canvas_widget.coords(self.obstacle19)[3] - 3]

        # Obstacle 20
        # Defining the center of obstacle 2
        obstacle20_center = self.o + np.array([pixels * 16, pixels * 1])
        # Building the obstacle 20
        self.obstacle20 = self.canvas_widget.create_rectangle(
            obstacle20_center[0] - 10, obstacle20_center[1] - 10,  # Top left corner
            obstacle20_center[0] + 10, obstacle20_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 20 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle20 = [self.canvas_widget.coords(self.obstacle20)[0] + 3,
         self.canvas_widget.coords(self.obstacle20)[1] + 3,
         self.canvas_widget.coords(self.obstacle20)[2] - 3,
         self.canvas_widget.coords(self.obstacle20)[3] - 3]

        # Obstacle 21
        # Defining the center of obstacle 21
        obstacle21_center = self.o + np.array([pixels * 17, pixels * 1])
        # Building the obstacle 21
        self.obstacle21 = self.canvas_widget.create_rectangle(
            obstacle21_center[0] - 10, obstacle21_center[1] - 10,  # Top left corner
            obstacle21_center[0] + 10, obstacle21_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 21 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle21 = [self.canvas_widget.coords(self.obstacle21)[0] + 3,
         self.canvas_widget.coords(self.obstacle21)[1] + 3,
         self.canvas_widget.coords(self.obstacle21)[2] - 3,
         self.canvas_widget.coords(self.obstacle21)[3] - 3]

        # Obstacle 22
        # Defining the center of obstacle 22
        obstacle22_center = self.o + np.array([pixels * 18, pixels * 1])
        # Building the obstacle 22
        self.obstacle22 = self.canvas_widget.create_rectangle(
            obstacle22_center[0] - 10, obstacle22_center[1] - 10,  # Top left corner
            obstacle22_center[0] + 10, obstacle22_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 22 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle22 = [self.canvas_widget.coords(self.obstacle22)[0] + 3,
         self.canvas_widget.coords(self.obstacle22)[1] + 3,
         self.canvas_widget.coords(self.obstacle22)[2] - 3,
         self.canvas_widget.coords(self.obstacle22)[3] - 3]

        # Obstacle 23
        # Defining the center of obstacle 23
        obstacle23_center = self.o + np.array([pixels * 18, pixels * 2])
        # Building the obstacle 23
        self.obstacle23 = self.canvas_widget.create_rectangle(
            obstacle23_center[0] - 10, obstacle23_center[1] - 10,  # Top left corner
            obstacle23_center[0] + 10, obstacle23_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 23 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle23 = [self.canvas_widget.coords(self.obstacle23)[0] + 3,
         self.canvas_widget.coords(self.obstacle23)[1] + 3,
         self.canvas_widget.coords(self.obstacle23)[2] - 3,
         self.canvas_widget.coords(self.obstacle23)[3] - 3]

        # Obstacle 24
        # Defining the center of obstacle 24
        obstacle24_center = self.o + np.array([pixels * 18, pixels * 3])
        # Building the obstacle 24
        self.obstacle24 = self.canvas_widget.create_rectangle(
            obstacle24_center[0] - 10, obstacle24_center[1] - 10,  # Top left corner
            obstacle24_center[0] + 10, obstacle24_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 24 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle24 = [self.canvas_widget.coords(self.obstacle24)[0] + 3,
         self.canvas_widget.coords(self.obstacle24)[1] + 3,
         self.canvas_widget.coords(self.obstacle24)[2] - 3,
         self.canvas_widget.coords(self.obstacle24)[3] - 3]

        # Obstacle 25
        # Defining the center of obstacle 25
        obstacle25_center = self.o + np.array([pixels * 18, pixels * 7])
        # Building the obstacle 25
        self.obstacle25 = self.canvas_widget.create_rectangle(
            obstacle25_center[0] - 10, obstacle25_center[1] - 10,  # Top left corner
            obstacle25_center[0] + 10, obstacle25_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 25 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle25 = [self.canvas_widget.coords(self.obstacle25)[0] + 3,
         self.canvas_widget.coords(self.obstacle25)[1] + 3,
         self.canvas_widget.coords(self.obstacle25)[2] - 3,
         self.canvas_widget.coords(self.obstacle25)[3] - 3]

        # Obstacle 26
        # Defining the center of obstacle 26
        obstacle26_center = self.o + np.array([pixels * 18, pixels * 8])
        # Building the obstacle 26
        self.obstacle26 = self.canvas_widget.create_rectangle(
            obstacle26_center[0] - 10, obstacle26_center[1] - 10,  # Top left corner
            obstacle26_center[0] + 10, obstacle26_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 26 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle26 = [self.canvas_widget.coords(self.obstacle26)[0] + 3,
         self.canvas_widget.coords(self.obstacle26)[1] + 3,
         self.canvas_widget.coords(self.obstacle26)[2] - 3,
         self.canvas_widget.coords(self.obstacle26)[3] - 3]

        # Obstacle 27
        # Defining the center of obstacle 27
        obstacle27_center = self.o + np.array([pixels * 19, pixels * 8])
        # Building the obstacle 27
        self.obstacle27 = self.canvas_widget.create_rectangle(
            obstacle27_center[0] - 10, obstacle27_center[1] - 10,  # Top left corner
            obstacle27_center[0] + 10, obstacle27_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 27 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle27 = [self.canvas_widget.coords(self.obstacle27)[0] + 3,
         self.canvas_widget.coords(self.obstacle27)[1] + 3,
         self.canvas_widget.coords(self.obstacle27)[2] - 3,
         self.canvas_widget.coords(self.obstacle27)[3] - 3]

        # Obstacle 28
        # Defining the center of obstacle 28
        obstacle28_center = self.o + np.array([pixels * 20, pixels * 8])
        # Building the obstacle 28
        self.obstacle28 = self.canvas_widget.create_rectangle(
            obstacle28_center[0] - 10, obstacle28_center[1] - 10,  # Top left corner
            obstacle28_center[0] + 10, obstacle28_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 28 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle28 = [self.canvas_widget.coords(self.obstacle28)[0] + 3,
         self.canvas_widget.coords(self.obstacle28)[1] + 3,
         self.canvas_widget.coords(self.obstacle28)[2] - 3,
         self.canvas_widget.coords(self.obstacle28)[3] - 3]

        # Obstacle 29
        # Defining the center of obstacle 29
        obstacle29_center = self.o + np.array([pixels * 21, pixels * 8])
        # Building the obstacle 29
        self.obstacle29 = self.canvas_widget.create_rectangle(
            obstacle29_center[0] - 10, obstacle29_center[1] - 10,  # Top left corner
            obstacle29_center[0] + 10, obstacle29_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 29 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle29 = [self.canvas_widget.coords(self.obstacle29)[0] + 3,
         self.canvas_widget.coords(self.obstacle29)[1] + 3,
         self.canvas_widget.coords(self.obstacle29)[2] - 3,
         self.canvas_widget.coords(self.obstacle29)[3] - 3]

        # Obstacle 30
        # Defining the center of obstacle 30
        obstacle30_center = self.o + np.array([pixels * 22, pixels * 8])
        # Building the obstacle 30
        self.obstacle30 = self.canvas_widget.create_rectangle(
            obstacle30_center[0] - 10, obstacle30_center[1] - 10,  # Top left corner
            obstacle30_center[0] + 10, obstacle30_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 30 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle30 = [self.canvas_widget.coords(self.obstacle30)[0] + 3,
         self.canvas_widget.coords(self.obstacle30)[1] + 3,
         self.canvas_widget.coords(self.obstacle30)[2] - 3,
         self.canvas_widget.coords(self.obstacle30)[3] - 3]

        # Obstacle 31
        # Defining the center of obstacle 31
        obstacle31_center = self.o + np.array([pixels * 22, pixels * 7])
        # Building the obstacle 31
        self.obstacle31 = self.canvas_widget.create_rectangle(
            obstacle31_center[0] - 10, obstacle31_center[1] - 10,  # Top left corner
            obstacle31_center[0] + 10, obstacle31_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 31 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle31 = [self.canvas_widget.coords(self.obstacle31)[0] + 3,
         self.canvas_widget.coords(self.obstacle31)[1] + 3,
         self.canvas_widget.coords(self.obstacle31)[2] - 3,
         self.canvas_widget.coords(self.obstacle31)[3] - 3]

        # Obstacle 32
        # Defining the center of obstacle 32
        obstacle32_center = self.o + np.array([pixels * 22, pixels * 6])
        # Building the obstacle 32
        self.obstacle32 = self.canvas_widget.create_rectangle(
            obstacle32_center[0] - 10, obstacle32_center[1] - 10,  # Top left corner
            obstacle32_center[0] + 10, obstacle32_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 32 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle32 = [self.canvas_widget.coords(self.obstacle32)[0] + 3,
         self.canvas_widget.coords(self.obstacle32)[1] + 3,
         self.canvas_widget.coords(self.obstacle32)[2] - 3,
         self.canvas_widget.coords(self.obstacle32)[3] - 3]

        # Obstacle 33
        # Defining the center of obstacle 33
        obstacle33_center = self.o + np.array([pixels * 23, pixels * 2])
        # Building the obstacle 33
        self.obstacle33 = self.canvas_widget.create_rectangle(
            obstacle33_center[0] - 10, obstacle33_center[1] - 10,  # Top left corner
            obstacle33_center[0] + 10, obstacle33_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 33 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle33 = [self.canvas_widget.coords(self.obstacle33)[0] + 3,
         self.canvas_widget.coords(self.obstacle33)[1] + 3,
         self.canvas_widget.coords(self.obstacle33)[2] - 3,
         self.canvas_widget.coords(self.obstacle33)[3] - 3]

        # Obstacle 34
        # Defining the center of obstacle 34
        obstacle34_center = self.o + np.array([pixels * 24, pixels * 2])
        # Building the obstacle 34
        self.obstacle34 = self.canvas_widget.create_rectangle(
            obstacle34_center[0] - 10, obstacle34_center[1] - 10,  # Top left corner
            obstacle34_center[0] + 10, obstacle34_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 34 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle34 = [self.canvas_widget.coords(self.obstacle34)[0] + 3,
         self.canvas_widget.coords(self.obstacle34)[1] + 3,
         self.canvas_widget.coords(self.obstacle34)[2] - 3,
         self.canvas_widget.coords(self.obstacle34)[3] - 3]

        # Obstacle 35
        # Defining the center of obstacle 35
        obstacle35_center = self.o + np.array([pixels * 25, pixels * 2])
        # Building the obstacle 35
        self.obstacle35 = self.canvas_widget.create_rectangle(
            obstacle35_center[0] - 10, obstacle35_center[1] - 10,  # Top left corner
            obstacle35_center[0] + 10, obstacle35_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 35 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle35 = [self.canvas_widget.coords(self.obstacle35)[0] + 3,
         self.canvas_widget.coords(self.obstacle35)[1] + 3,
         self.canvas_widget.coords(self.obstacle35)[2] - 3,
         self.canvas_widget.coords(self.obstacle35)[3] - 3]

        # Obstacle 36
        # Defining the center of obstacle 36
        obstacle36_center = self.o + np.array([pixels * 26, pixels * 2])
        # Building the obstacle 36
        self.obstacle36 = self.canvas_widget.create_rectangle(
            obstacle36_center[0] - 10, obstacle36_center[1] - 10,  # Top left corner
            obstacle36_center[0] + 10, obstacle36_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 36 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle36 = [self.canvas_widget.coords(self.obstacle36)[0] + 3,
         self.canvas_widget.coords(self.obstacle36)[1] + 3,
         self.canvas_widget.coords(self.obstacle36)[2] - 3,
         self.canvas_widget.coords(self.obstacle36)[3] - 3]

        # Obstacle 37
        # Defining the center of obstacle 37
        obstacle37_center = self.o + np.array([pixels * 26, pixels * 3])
        # Building the obstacle 37
        self.obstacle37 = self.canvas_widget.create_rectangle(
            obstacle37_center[0] - 10, obstacle37_center[1] - 10,  # Top left corner
            obstacle37_center[0] + 10, obstacle37_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 37 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle37 = [self.canvas_widget.coords(self.obstacle37)[0] + 3,
         self.canvas_widget.coords(self.obstacle37)[1] + 3,
         self.canvas_widget.coords(self.obstacle37)[2] - 3,
         self.canvas_widget.coords(self.obstacle37)[3] - 3]

        # Obstacle 38
        # Defining the center of obstacle 38
        obstacle38_center = self.o + np.array([pixels * 26, pixels * 4])
        # Building the obstacle 38
        self.obstacle38 = self.canvas_widget.create_rectangle(
            obstacle38_center[0] - 10, obstacle38_center[1] - 10,  # Top left corner
            obstacle38_center[0] + 10, obstacle38_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 38 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle38 = [self.canvas_widget.coords(self.obstacle38)[0] + 3,
         self.canvas_widget.coords(self.obstacle38)[1] + 3,
         self.canvas_widget.coords(self.obstacle38)[2] - 3,
         self.canvas_widget.coords(self.obstacle38)[3] - 3]

        # Obstacle 39
        # Defining the center of obstacle 39
        obstacle39_center = self.o + np.array([pixels * 26, pixels * 5])
        # Building the obstacle 39
        self.obstacle39 = self.canvas_widget.create_rectangle(
            obstacle39_center[0] - 10, obstacle39_center[1] - 10,  # Top left corner
            obstacle39_center[0] + 10, obstacle39_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 39 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle39 = [self.canvas_widget.coords(self.obstacle39)[0] + 3,
         self.canvas_widget.coords(self.obstacle39)[1] + 3,
         self.canvas_widget.coords(self.obstacle39)[2] - 3,
         self.canvas_widget.coords(self.obstacle39)[3] - 3]

        # Obstacle 40
        # Defining the center of obstacle 40
        obstacle40_center = self.o + np.array([pixels * 27, pixels * 5])
        # Building the obstacle 40
        self.obstacle40 = self.canvas_widget.create_rectangle(
            obstacle40_center[0] - 10, obstacle40_center[1] - 10,  # Top left corner
            obstacle40_center[0] + 10, obstacle40_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 40 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle40 = [self.canvas_widget.coords(self.obstacle40)[0] + 3,
         self.canvas_widget.coords(self.obstacle40)[1] + 3,
         self.canvas_widget.coords(self.obstacle40)[2] - 3,
         self.canvas_widget.coords(self.obstacle40)[3] - 3]

        # Obstacle 41
        # Defining the center of obstacle 41
        obstacle41_center = self.o + np.array([pixels * 27, pixels * 7])
        # Building the obstacle 41
        self.obstacle41 = self.canvas_widget.create_rectangle(
            obstacle41_center[0] - 10, obstacle41_center[1] - 10,  # Top left corner
            obstacle41_center[0] + 10, obstacle41_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 41 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle41 = [self.canvas_widget.coords(self.obstacle41)[0] + 3,
         self.canvas_widget.coords(self.obstacle41)[1] + 3,
         self.canvas_widget.coords(self.obstacle41)[2] - 3,
         self.canvas_widget.coords(self.obstacle41)[3] - 3]

        # Obstacle 42
        # Defining the center of obstacle 42
        obstacle42_center = self.o + np.array([pixels * 28, pixels * 7])
        # Building the obstacle 42
        self.obstacle42 = self.canvas_widget.create_rectangle(
            obstacle42_center[0] - 10, obstacle42_center[1] - 10,  # Top left corner
            obstacle42_center[0] + 10, obstacle42_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 42 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle42 = [self.canvas_widget.coords(self.obstacle42)[0] + 3,
         self.canvas_widget.coords(self.obstacle42)[1] + 3,
         self.canvas_widget.coords(self.obstacle42)[2] - 3,
         self.canvas_widget.coords(self.obstacle42)[3] - 3]

        # Obstacle 43
        # Defining the center of obstacle 43
        obstacle43_center = self.o + np.array([pixels * 26, pixels * 7])
        # Building the obstacle 43
        self.obstacle43 = self.canvas_widget.create_rectangle(
            obstacle43_center[0] - 10, obstacle43_center[1] - 10,  # Top left corner
            obstacle43_center[0] + 10, obstacle43_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 43 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle43 = [self.canvas_widget.coords(self.obstacle43)[0] + 3,
         self.canvas_widget.coords(self.obstacle43)[1] + 3,
         self.canvas_widget.coords(self.obstacle43)[2] - 3,
         self.canvas_widget.coords(self.obstacle43)[3] - 3]

        # Obstacle 44
        # Defining the center of obstacle 44
        obstacle44_center = self.o + np.array([pixels * 27, pixels * 8])
        # Building the obstacle 44
        self.obstacle44 = self.canvas_widget.create_rectangle(
            obstacle44_center[0] - 10, obstacle44_center[1] - 10,  # Top left corner
            obstacle44_center[0] + 10, obstacle44_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 44 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle44 = [self.canvas_widget.coords(self.obstacle44)[0] + 3,
         self.canvas_widget.coords(self.obstacle44)[1] + 3,
         self.canvas_widget.coords(self.obstacle44)[2] - 3,
         self.canvas_widget.coords(self.obstacle44)[3] - 3]

        # Obstacle 45
        # Defining the center of obstacle 45
        obstacle45_center = self.o + np.array([pixels * 27, pixels * 9])
        # Building the obstacle 45
        self.obstacle45 = self.canvas_widget.create_rectangle(
            obstacle45_center[0] - 10, obstacle45_center[1] - 10,  # Top left corner
            obstacle45_center[0] + 10, obstacle45_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 45 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle45 = [self.canvas_widget.coords(self.obstacle45)[0] + 3,
         self.canvas_widget.coords(self.obstacle45)[1] + 3,
         self.canvas_widget.coords(self.obstacle45)[2] - 3,
         self.canvas_widget.coords(self.obstacle45)[3] - 3]

        # Obstacle 46
        # Defining the center of obstacle 46
        obstacle46_center = self.o + np.array([pixels * 27, pixels * 10])
        # Building the obstacle 46
        self.obstacle46 = self.canvas_widget.create_rectangle(
            obstacle46_center[0] - 10, obstacle46_center[1] - 10,  # Top left corner
            obstacle46_center[0] + 10, obstacle46_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 46 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle46 = [self.canvas_widget.coords(self.obstacle46)[0] + 3,
         self.canvas_widget.coords(self.obstacle46)[1] + 3,
         self.canvas_widget.coords(self.obstacle46)[2] - 3,
         self.canvas_widget.coords(self.obstacle46)[3] - 3]

        # Obstacle 47
        # Defining the center of obstacle 47
        obstacle47_center = self.o + np.array([pixels * 27, pixels * 11])
        # Building the obstacle 47
        self.obstacle47 = self.canvas_widget.create_rectangle(
            obstacle47_center[0] - 10, obstacle47_center[1] - 10,  # Top left corner
            obstacle47_center[0] + 10, obstacle47_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 47 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle47 = [self.canvas_widget.coords(self.obstacle47)[0] + 3,
         self.canvas_widget.coords(self.obstacle47)[1] + 3,
         self.canvas_widget.coords(self.obstacle47)[2] - 3,
         self.canvas_widget.coords(self.obstacle47)[3] - 3]

        # Obstacle 48
        # Defining the center of obstacle 48
        obstacle48_center = self.o + np.array([pixels * 26, pixels * 11])
        # Building the obstacle 48
        self.obstacle48 = self.canvas_widget.create_rectangle(
            obstacle48_center[0] - 10, obstacle48_center[1] - 10,  # Top left corner
            obstacle48_center[0] + 10, obstacle48_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 48 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle48 = [self.canvas_widget.coords(self.obstacle48)[0] + 3,
         self.canvas_widget.coords(self.obstacle48)[1] + 3,
         self.canvas_widget.coords(self.obstacle48)[2] - 3,
         self.canvas_widget.coords(self.obstacle48)[3] - 3]

        # Obstacle 49
        # Defining the center of obstacle 49
        obstacle49_center = self.o + np.array([pixels * 28, pixels * 11])
        # Building the obstacle 49
        self.obstacle49 = self.canvas_widget.create_rectangle(
            obstacle49_center[0] - 10, obstacle49_center[1] - 10,  # Top left corner
            obstacle49_center[0] + 10, obstacle49_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 49 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle49 = [self.canvas_widget.coords(self.obstacle49)[0] + 3,
         self.canvas_widget.coords(self.obstacle49)[1] + 3,
         self.canvas_widget.coords(self.obstacle49)[2] - 3,
         self.canvas_widget.coords(self.obstacle49)[3] - 3]

        # Obstacle 50
        # Defining the center of obstacle 50
        obstacle50_center = self.o + np.array([pixels * 23, pixels * 10])
        # Building the obstacle 50
        self.obstacle50 = self.canvas_widget.create_rectangle(
            obstacle50_center[0] - 10, obstacle50_center[1] - 10,  # Top left corner
            obstacle50_center[0] + 10, obstacle50_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 50 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle50 = [self.canvas_widget.coords(self.obstacle50)[0] + 3,
         self.canvas_widget.coords(self.obstacle50)[1] + 3,
         self.canvas_widget.coords(self.obstacle50)[2] - 3,
         self.canvas_widget.coords(self.obstacle50)[3] - 3]

        # Obstacle 51
        # Defining the center of obstacle 51
        obstacle51_center = self.o + np.array([pixels * 22, pixels * 10])
        # Building the obstacle 51
        self.obstacle51 = self.canvas_widget.create_rectangle(
            obstacle51_center[0] - 10, obstacle51_center[1] - 10,  # Top left corner
            obstacle51_center[0] + 10, obstacle51_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 51 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle51 = [self.canvas_widget.coords(self.obstacle51)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle51)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle51)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle51)[3] - 3]

        # Obstacle 52
        # Defining the center of obstacle 52
        obstacle52_center = self.o + np.array([pixels * 21, pixels * 10])
        # Building the obstacle 52
        self.obstacle52 = self.canvas_widget.create_rectangle(
            obstacle52_center[0] - 10, obstacle52_center[1] - 10,  # Top left corner
            obstacle52_center[0] + 10, obstacle52_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 52 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle52 = [self.canvas_widget.coords(self.obstacle52)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle52)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle52)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle52)[3] - 3]

        # Obstacle 53
        # Defining the center of obstacle 53
        obstacle53_center = self.o + np.array([pixels * 21, pixels * 11])
        # Building the obstacle 53
        self.obstacle53 = self.canvas_widget.create_rectangle(
            obstacle53_center[0] - 10, obstacle53_center[1] - 10,  # Top left corner
            obstacle53_center[0] + 10, obstacle53_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 53 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle53 = [self.canvas_widget.coords(self.obstacle53)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle53)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle53)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle53)[3] - 3]

        # Obstacle 54
        # Defining the center of obstacle 54
        obstacle54_center = self.o + np.array([pixels * 21, pixels * 12])
        # Building the obstacle 54
        self.obstacle54 = self.canvas_widget.create_rectangle(
            obstacle54_center[0] - 10, obstacle54_center[1] - 10,  # Top left corner
            obstacle54_center[0] + 10, obstacle54_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 54 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle54 = [self.canvas_widget.coords(self.obstacle54)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle54)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle54)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle54)[3] - 3]

        # Obstacle 55
        # Defining the center of obstacle 55
        obstacle55_center = self.o + np.array([pixels * 21, pixels * 13])
        # Building the obstacle 55
        self.obstacle55 = self.canvas_widget.create_rectangle(
            obstacle55_center[0] - 10, obstacle55_center[1] - 10,  # Top left corner
            obstacle55_center[0] + 10, obstacle55_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 55 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle55 = [self.canvas_widget.coords(self.obstacle55)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle55)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle55)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle55)[3] - 3]

        # Obstacle 56
        # Defining the center of obstacle 56
        obstacle56_center = self.o + np.array([pixels * 18, pixels * 11])
        # Building the obstacle 56
        self.obstacle56 = self.canvas_widget.create_rectangle(
            obstacle56_center[0] - 10, obstacle56_center[1] - 10,  # Top left corner
            obstacle56_center[0] + 10, obstacle56_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 56 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle56 = [self.canvas_widget.coords(self.obstacle56)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle56)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle56)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle56)[3] - 3]

        # Obstacle 57
        # Defining the center of obstacle 57
        obstacle57_center = self.o + np.array([pixels * 17, pixels * 11])
        # Building the obstacle 57
        self.obstacle57 = self.canvas_widget.create_rectangle(
            obstacle57_center[0] - 10, obstacle57_center[1] - 10,  # Top left corner
            obstacle57_center[0] + 10, obstacle57_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 57 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle57 = [self.canvas_widget.coords(self.obstacle57)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle57)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle57)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle57)[3] - 3]

        # Obstacle 58
        # Defining the center of obstacle 58
        obstacle58_center = self.o + np.array([pixels * 16, pixels * 11])
        # Building the obstacle 58
        self.obstacle58 = self.canvas_widget.create_rectangle(
            obstacle58_center[0] - 10, obstacle58_center[1] - 10,  # Top left corner
            obstacle58_center[0] + 10, obstacle58_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 58 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle58 = [self.canvas_widget.coords(self.obstacle58)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle58)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle58)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle58)[3] - 3]

        # Obstacle 59
        # Defining the center of obstacle 59
        obstacle59_center = self.o + np.array([pixels * 15, pixels * 11])
        # Building the obstacle 59
        self.obstacle59 = self.canvas_widget.create_rectangle(
            obstacle59_center[0] - 10, obstacle59_center[1] - 10,  # Top left corner
            obstacle59_center[0] + 10, obstacle59_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 59 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle59 = [self.canvas_widget.coords(self.obstacle59)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle59)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle59)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle59)[3] - 3]

        # Obstacle 60
        # Defining the center of obstacle 60
        obstacle60_center = self.o + np.array([pixels * 14, pixels * 11])
        # Building the obstacle 60
        self.obstacle60 = self.canvas_widget.create_rectangle(
            obstacle60_center[0] - 10, obstacle60_center[1] - 10,  # Top left corner
            obstacle60_center[0] + 10, obstacle60_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 60 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle60 = [self.canvas_widget.coords(self.obstacle60)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle60)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle60)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle60)[3] - 3]

        # Obstacle 61
        # Defining the center of obstacle 61
        obstacle61_center = self.o + np.array([pixels * 14, pixels * 10])
        # Building the obstacle 61
        self.obstacle61 = self.canvas_widget.create_rectangle(
            obstacle61_center[0] - 10, obstacle61_center[1] - 10,  # Top left corner
            obstacle61_center[0] + 10, obstacle61_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 61 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle61 = [self.canvas_widget.coords(self.obstacle61)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle61)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle61)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle61)[3] - 3]

        # Obstacle 62
        # Defining the center of obstacle 62
        obstacle62_center = self.o + np.array([pixels * 10, pixels * 9])
        # Building the obstacle 62
        self.obstacle62 = self.canvas_widget.create_rectangle(
            obstacle62_center[0] - 10, obstacle62_center[1] - 10,  # Top left corner
            obstacle62_center[0] + 10, obstacle62_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 62 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle62 = [self.canvas_widget.coords(self.obstacle62)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle62)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle62)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle62)[3] - 3]

        # Obstacle 63
        # Defining the center of obstacle 63
        obstacle63_center = self.o + np.array([pixels * 9, pixels * 9])
        # Building the obstacle 63
        self.obstacle63 = self.canvas_widget.create_rectangle(
            obstacle63_center[0] - 10, obstacle63_center[1] - 10,  # Top left corner
            obstacle63_center[0] + 10, obstacle63_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 63 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle63 = [self.canvas_widget.coords(self.obstacle63)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle63)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle63)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle63)[3] - 3]

        # Obstacle 64
        # Defining the center of obstacle 64
        obstacle64_center = self.o + np.array([pixels * 8, pixels * 9])
        # Building the obstacle 64
        self.obstacle64 = self.canvas_widget.create_rectangle(
            obstacle64_center[0] - 10, obstacle64_center[1] - 10,  # Top left corner
            obstacle64_center[0] + 10, obstacle64_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 64 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle64 = [self.canvas_widget.coords(self.obstacle64)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle64)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle64)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle64)[3] - 3]

        # Obstacle 65
        # Defining the center of obstacle 65
        obstacle65_center = self.o + np.array([pixels * 7, pixels * 9])
        # Building the obstacle 65
        self.obstacle65 = self.canvas_widget.create_rectangle(
            obstacle65_center[0] - 10, obstacle65_center[1] - 10,  # Top left corner
            obstacle65_center[0] + 10, obstacle65_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 65 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle65 = [self.canvas_widget.coords(self.obstacle65)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle65)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle65)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle65)[3] - 3]

        # Obstacle 66
        # Defining the center of obstacle 66
        obstacle66_center = self.o + np.array([pixels * 7, pixels * 8])
        # Building the obstacle 66
        self.obstacle66 = self.canvas_widget.create_rectangle(
            obstacle66_center[0] - 10, obstacle66_center[1] - 10,  # Top left corner
            obstacle66_center[0] + 10, obstacle66_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 66 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle66 = [self.canvas_widget.coords(self.obstacle66)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle66)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle66)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle66)[3] - 3]

        # Obstacle 67
        # Defining the center of obstacle 67
        obstacle67_center = self.o + np.array([pixels * 7, pixels * 7])
        # Building the obstacle 67
        self.obstacle67 = self.canvas_widget.create_rectangle(
            obstacle67_center[0] - 10, obstacle67_center[1] - 10,  # Top left corner
            obstacle67_center[0] + 10, obstacle67_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 67 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle67 = [self.canvas_widget.coords(self.obstacle67)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle67)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle67)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle67)[3] - 3]

        # Obstacle 68
        # Defining the center of obstacle 68
        obstacle68_center = self.o + np.array([pixels * 6, pixels * 7])
        # Building the obstacle 68
        self.obstacle68 = self.canvas_widget.create_rectangle(
            obstacle68_center[0] - 10, obstacle68_center[1] - 10,  # Top left corner
            obstacle68_center[0] + 10, obstacle68_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 68 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle68 = [self.canvas_widget.coords(self.obstacle68)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle68)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle68)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle68)[3] - 3]

        # Obstacle 69
        # Defining the center of obstacle 69
        obstacle69_center = self.o + np.array([pixels * 5, pixels * 7])
        # Building the obstacle 69
        self.obstacle69 = self.canvas_widget.create_rectangle(
            obstacle69_center[0] - 10, obstacle69_center[1] - 10,  # Top left corner
            obstacle69_center[0] + 10, obstacle69_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 69 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle69 = [self.canvas_widget.coords(self.obstacle69)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle69)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle69)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle69)[3] - 3]

        # Obstacle 70
        # Defining the center of obstacle 70
        obstacle70_center = self.o + np.array([pixels * 5, pixels * 5])
        # Building the obstacle 70
        self.obstacle70 = self.canvas_widget.create_rectangle(
            obstacle70_center[0] - 10, obstacle70_center[1] - 10,  # Top left corner
            obstacle70_center[0] + 10, obstacle70_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 70 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle70 = [self.canvas_widget.coords(self.obstacle70)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle70)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle70)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle70)[3] - 3]

        # Obstacle 71
        # Defining the center of obstacle 71
        obstacle71_center = self.o + np.array([pixels * 5, pixels * 6])
        # Building the obstacle 71
        self.obstacle71 = self.canvas_widget.create_rectangle(
            obstacle71_center[0] - 10, obstacle71_center[1] - 10,  # Top left corner
            obstacle71_center[0] + 10, obstacle71_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 71 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle71 = [self.canvas_widget.coords(self.obstacle71)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle71)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle71)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle71)[3] - 3]

        # Obstacle 72
        # Defining the center of obstacle 72
        obstacle72_center = self.o + np.array([pixels, pixels * 7])
        # Building the obstacle 72
        self.obstacle72 = self.canvas_widget.create_rectangle(
            obstacle72_center[0] - 10, obstacle72_center[1] - 10,  # Top left corner
            obstacle72_center[0] + 10, obstacle72_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 72 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle72 = [self.canvas_widget.coords(self.obstacle72)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle72)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle72)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle72)[3] - 3]

        # Obstacle 73
        # Defining the center of obstacle 73
        obstacle73_center = self.o + np.array([pixels, pixels * 6])
        # Building the obstacle 73
        self.obstacle73 = self.canvas_widget.create_rectangle(
            obstacle73_center[0] - 10, obstacle73_center[1] - 10,  # Top left corner
            obstacle73_center[0] + 10, obstacle73_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 73 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle73 = [self.canvas_widget.coords(self.obstacle73)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle73)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle73)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle73)[3] - 3]

        # Obstacle 74
        # Defining the center of obstacle 74
        obstacle74_center = self.o + np.array([pixels * 2, pixels * 6])
        # Building the obstacle 74
        self.obstacle74 = self.canvas_widget.create_rectangle(
            obstacle74_center[0] - 10, obstacle74_center[1] - 10,  # Top left corner
            obstacle74_center[0] + 10, obstacle74_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 74 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle74 = [self.canvas_widget.coords(self.obstacle74)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle74)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle74)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle74)[3] - 3]

        # Obstacle 75
        # Defining the center of obstacle 75
        obstacle75_center = self.o + np.array([pixels, pixels * 8])
        # Building the obstacle 75
        self.obstacle75 = self.canvas_widget.create_rectangle(
            obstacle75_center[0] - 10, obstacle75_center[1] - 10,  # Top left corner
            obstacle75_center[0] + 10, obstacle75_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 75 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle75 = [self.canvas_widget.coords(self.obstacle75)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle75)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle75)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle75)[3] - 3]

        # Obstacle 76
        # Defining the center of obstacle 76
        obstacle76_center = self.o + np.array([pixels, pixels * 9])
        # Building the obstacle 76
        self.obstacle76 = self.canvas_widget.create_rectangle(
            obstacle76_center[0] - 10, obstacle76_center[1] - 10,  # Top left corner
            obstacle76_center[0] + 10, obstacle76_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 76 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle76 = [self.canvas_widget.coords(self.obstacle76)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle76)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle76)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle76)[3] - 3]

        # Obstacle 77
        # Defining the center of obstacle 77
        obstacle77_center = self.o + np.array([pixels, pixels * 10])
        # Building the obstacle 77
        self.obstacle77 = self.canvas_widget.create_rectangle(
            obstacle77_center[0] - 10, obstacle77_center[1] - 10,  # Top left corner
            obstacle77_center[0] + 10, obstacle77_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 77 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle77 = [self.canvas_widget.coords(self.obstacle77)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle77)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle77)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle77)[3] - 3]

        # Obstacle 78
        # Defining the center of obstacle 78
        obstacle78_center = self.o + np.array([pixels, pixels * 11])
        # Building the obstacle 78
        self.obstacle78 = self.canvas_widget.create_rectangle(
            obstacle78_center[0] - 10, obstacle78_center[1] - 10,  # Top left corner
            obstacle78_center[0] + 10, obstacle78_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 78 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle78 = [self.canvas_widget.coords(self.obstacle78)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle78)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle78)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle78)[3] - 3]

        # Obstacle 79
        # Defining the center of obstacle 79
        obstacle79_center = self.o + np.array([pixels * 3, pixels * 9])
        # Building the obstacle 79
        self.obstacle79 = self.canvas_widget.create_rectangle(
            obstacle79_center[0] - 10, obstacle79_center[1] - 10,  # Top left corner
            obstacle79_center[0] + 10, obstacle79_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 79 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle79 = [self.canvas_widget.coords(self.obstacle79)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle79)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle79)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle79)[3] - 3]

        # Obstacle 80
        # Defining the center of obstacle 80
        obstacle80_center = self.o + np.array([pixels * 3, pixels * 10])
        # Building the obstacle 80
        self.obstacle80 = self.canvas_widget.create_rectangle(
            obstacle80_center[0] - 10, obstacle80_center[1] - 10,  # Top left corner
            obstacle80_center[0] + 10, obstacle80_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 80 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle80 = [self.canvas_widget.coords(self.obstacle80)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle80)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle80)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle80)[3] - 3]

        # Obstacle 81
        # Defining the center of obstacle 81
        obstacle81_center = self.o + np.array([pixels * 3, pixels * 11])
        # Building the obstacle 81
        self.obstacle81 = self.canvas_widget.create_rectangle(
            obstacle81_center[0] - 10, obstacle81_center[1] - 10,  # Top left corner
            obstacle81_center[0] + 10, obstacle81_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 81 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle81 = [self.canvas_widget.coords(self.obstacle81)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle81)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle81)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle81)[3] - 3]

        # Obstacle 82
        # Defining the center of obstacle 82
        obstacle82_center = self.o + np.array([pixels * 3, pixels * 12])
        # Building the obstacle 82
        self.obstacle82 = self.canvas_widget.create_rectangle(
            obstacle82_center[0] - 10, obstacle82_center[1] - 10,  # Top left corner
            obstacle82_center[0] + 10, obstacle82_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 82 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle82 = [self.canvas_widget.coords(self.obstacle82)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle82)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle82)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle82)[3] - 3]

        # Obstacle 83
        # Defining the center of obstacle 83
        obstacle83_center = self.o + np.array([pixels * 3, pixels * 13])
        # Building the obstacle 83
        self.obstacle83 = self.canvas_widget.create_rectangle(
            obstacle83_center[0] - 10, obstacle83_center[1] - 10,  # Top left corner
            obstacle83_center[0] + 10, obstacle83_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 83 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle83 = [self.canvas_widget.coords(self.obstacle83)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle83)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle83)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle83)[3] - 3]

        # Obstacle 84
        # Defining the center of obstacle 84
        obstacle84_center = self.o + np.array([pixels * 4, pixels * 13])
        # Building the obstacle 84
        self.obstacle84 = self.canvas_widget.create_rectangle(
            obstacle84_center[0] - 10, obstacle84_center[1] - 10,  # Top left corner
            obstacle84_center[0] + 10, obstacle84_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 84 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle84 = [self.canvas_widget.coords(self.obstacle84)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle84)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle84)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle84)[3] - 3]

        # Obstacle 85
        # Defining the center of obstacle 85
        obstacle85_center = self.o + np.array([pixels * 5, pixels * 13])
        # Building the obstacle 85
        self.obstacle85 = self.canvas_widget.create_rectangle(
            obstacle85_center[0] - 10, obstacle85_center[1] - 10,  # Top left corner
            obstacle85_center[0] + 10, obstacle85_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 85 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle85 = [self.canvas_widget.coords(self.obstacle85)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle85)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle85)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle85)[3] - 3]

        # Obstacle 86
        # Defining the center of obstacle 86
        obstacle86_center = self.o + np.array([pixels * 6, pixels * 13])
        # Building the obstacle 86
        self.obstacle86 = self.canvas_widget.create_rectangle(
            obstacle86_center[0] - 10, obstacle86_center[1] - 10,  # Top left corner
            obstacle86_center[0] + 10, obstacle86_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 86 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle86 = [self.canvas_widget.coords(self.obstacle86)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle86)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle86)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle86)[3] - 3]

        # Obstacle 87
        # Defining the center of obstacle 87
        obstacle87_center = self.o + np.array([pixels * 6, pixels * 12])
        # Building the obstacle 87
        self.obstacle87 = self.canvas_widget.create_rectangle(
            obstacle87_center[0] - 10, obstacle87_center[1] - 10,  # Top left corner
            obstacle87_center[0] + 10, obstacle87_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 87 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle87 = [self.canvas_widget.coords(self.obstacle87)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle87)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle87)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle87)[3] - 3]

        # Obstacle 88
        # Defining the center of obstacle 88
        obstacle88_center = self.o + np.array([pixels * 2, pixels * 15])
        # Building the obstacle 88
        self.obstacle88 = self.canvas_widget.create_rectangle(
            obstacle88_center[0] - 10, obstacle88_center[1] - 10,  # Top left corner
            obstacle88_center[0] + 10, obstacle88_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 88 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle88 = [self.canvas_widget.coords(self.obstacle88)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle88)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle88)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle88)[3] - 3]

        # Obstacle 89
        # Defining the center of obstacle 89
        obstacle89_center = self.o + np.array([pixels * 2, pixels * 16])
        # Building the obstacle 89
        self.obstacle89 = self.canvas_widget.create_rectangle(
            obstacle89_center[0] - 10, obstacle89_center[1] - 10,  # Top left corner
            obstacle89_center[0] + 10, obstacle89_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 89 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle89 = [self.canvas_widget.coords(self.obstacle89)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle89)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle89)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle89)[3] - 3]

        # Obstacle 90
        # Defining the center of obstacle 90
        obstacle90_center = self.o + np.array([pixels * 2, pixels * 17])
        # Building the obstacle 90
        self.obstacle90 = self.canvas_widget.create_rectangle(
            obstacle90_center[0] - 10, obstacle90_center[1] - 10,  # Top left corner
            obstacle90_center[0] + 10, obstacle90_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 90 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle90 = [self.canvas_widget.coords(self.obstacle90)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle90)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle90)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle90)[3] - 3]

        # Obstacle 91
        # Defining the center of obstacle 91
        obstacle91_center = self.o + np.array([pixels * 2, pixels * 18])
        # Building the obstacle 91
        self.obstacle91 = self.canvas_widget.create_rectangle(
            obstacle91_center[0] - 10, obstacle91_center[1] - 10,  # Top left corner
            obstacle91_center[0] + 10, obstacle91_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 91 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle91 = [self.canvas_widget.coords(self.obstacle91)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle91)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle91)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle91)[3] - 3]

        # Obstacle 92
        # Defining the center of obstacle 92
        obstacle92_center = self.o + np.array([pixels * 2, pixels * 19])
        # Building the obstacle 92
        self.obstacle92 = self.canvas_widget.create_rectangle(
            obstacle92_center[0] - 10, obstacle92_center[1] - 10,  # Top left corner
            obstacle92_center[0] + 10, obstacle92_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 92 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle92 = [self.canvas_widget.coords(self.obstacle92)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle92)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle92)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle92)[3] - 3]

        # Obstacle 93
        # Defining the center of obstacle 93
        obstacle93_center = self.o + np.array([pixels, pixels * 16])
        # Building the obstacle 93
        self.obstacle93 = self.canvas_widget.create_rectangle(
            obstacle93_center[0] - 10, obstacle93_center[1] - 10,  # Top left corner
            obstacle93_center[0] + 10, obstacle93_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 93 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle93 = [self.canvas_widget.coords(self.obstacle93)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle93)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle93)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle93)[3] - 3]

        # Obstacle 94
        # Defining the center of obstacle 94
        obstacle94_center = self.o + np.array([pixels * 2, pixels * 21])
        # Building the obstacle 94
        self.obstacle94 = self.canvas_widget.create_rectangle(
            obstacle94_center[0] - 10, obstacle94_center[1] - 10,  # Top left corner
            obstacle94_center[0] + 10, obstacle94_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 94 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle94 = [self.canvas_widget.coords(self.obstacle94)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle94)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle94)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle94)[3] - 3]

        # Obstacle 95
        # Defining the center of obstacle 95
        obstacle95_center = self.o + np.array([pixels * 3, pixels * 21])
        # Building the obstacle 95
        self.obstacle95 = self.canvas_widget.create_rectangle(
            obstacle95_center[0] - 10, obstacle95_center[1] - 10,  # Top left corner
            obstacle95_center[0] + 10, obstacle95_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 95 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle95 = [self.canvas_widget.coords(self.obstacle95)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle95)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle95)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle95)[3] - 3]

        # Obstacle 96
        # Defining the center of obstacle 96
        obstacle96_center = self.o + np.array([pixels * 4, pixels * 21])
        # Building the obstacle 96
        self.obstacle96 = self.canvas_widget.create_rectangle(
            obstacle96_center[0] - 10, obstacle96_center[1] - 10,  # Top left corner
            obstacle96_center[0] + 10, obstacle96_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 96 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle96 = [self.canvas_widget.coords(self.obstacle96)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle96)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle96)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle96)[3] - 3]

        # Obstacle 97
        # Defining the center of obstacle 97
        obstacle97_center = self.o + np.array([pixels * 4, pixels * 22])
        # Building the obstacle 97
        self.obstacle97 = self.canvas_widget.create_rectangle(
            obstacle97_center[0] - 10, obstacle97_center[1] - 10,  # Top left corner
            obstacle97_center[0] + 10, obstacle97_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 97 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle97 = [self.canvas_widget.coords(self.obstacle97)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle97)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle97)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle97)[3] - 3]

        # Obstacle 98
        # Defining the center of obstacle 98
        obstacle98_center = self.o + np.array([pixels * 4, pixels * 23])
        # Building the obstacle 98
        self.obstacle98 = self.canvas_widget.create_rectangle(
            obstacle98_center[0] - 10, obstacle98_center[1] - 10,  # Top left corner
            obstacle98_center[0] + 10, obstacle98_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 98 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle98 = [self.canvas_widget.coords(self.obstacle98)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle98)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle98)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle98)[3] - 3]

        # Obstacle 99
        # Defining the center of obstacle 99
        obstacle99_center = self.o + np.array([pixels * 4, pixels * 24])
        # Building the obstacle 99
        self.obstacle99 = self.canvas_widget.create_rectangle(
            obstacle99_center[0] - 10, obstacle99_center[1] - 10,  # Top left corner
            obstacle99_center[0] + 10, obstacle99_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 99 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle99 = [self.canvas_widget.coords(self.obstacle99)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle99)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle99)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle99)[3] - 3]

        # Obstacle 100
        # Defining the center of obstacle 100
        obstacle100_center = self.o + np.array([pixels * 4, pixels * 25])
        # Building the obstacle 100
        self.obstacle100 = self.canvas_widget.create_rectangle(
            obstacle100_center[0] - 10, obstacle100_center[1] - 10,  # Top left corner
            obstacle100_center[0] + 10, obstacle100_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 100 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle100 = [self.canvas_widget.coords(self.obstacle100)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle100)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle100)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle100)[3] - 3]

        # Obstacle 101
        # Defining the center of obstacle 101
        obstacle101_center = self.o + np.array([pixels * 3, pixels * 25])
        # Building the obstacle 101
        self.obstacle101 = self.canvas_widget.create_rectangle(
            obstacle101_center[0] - 10, obstacle101_center[1] - 10,  # Top left corner
            obstacle101_center[0] + 10, obstacle101_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 101 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle101 = [self.canvas_widget.coords(self.obstacle101)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle101)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle101)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle101)[3] - 3]

        # Obstacle 102
        # Defining the center of obstacle 102
        obstacle102_center = self.o + np.array([pixels * 2, pixels * 25])
        # Building the obstacle 102
        self.obstacle102 = self.canvas_widget.create_rectangle(
            obstacle102_center[0] - 10, obstacle102_center[1] - 10,  # Top left corner
            obstacle102_center[0] + 10, obstacle102_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 102 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle102 = [self.canvas_widget.coords(self.obstacle102)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle102)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle102)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle102)[3] - 3]

        # Obstacle 103
        # Defining the center of obstacle 103
        obstacle103_center = self.o + np.array([pixels, pixels * 25])
        # Building the obstacle 103
        self.obstacle103 = self.canvas_widget.create_rectangle(
            obstacle103_center[0] - 10, obstacle103_center[1] - 10,  # Top left corner
            obstacle103_center[0] + 10, obstacle103_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 103 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle103 = [self.canvas_widget.coords(self.obstacle103)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle103)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle103)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle103)[3] - 3]

        # Obstacle 104
        # Defining the center of obstacle 104
        obstacle104_center = self.o + np.array([pixels * 3, pixels * 16])
        # Building the obstacle 104
        self.obstacle104 = self.canvas_widget.create_rectangle(
            obstacle104_center[0] - 10, obstacle104_center[1] - 10,  # Top left corner
            obstacle104_center[0] + 10, obstacle104_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 104 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle104 = [self.canvas_widget.coords(self.obstacle104)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle104)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle104)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle104)[3] - 3]

        # Obstacle 105
        # Defining the center of obstacle 105
        obstacle105_center = self.o + np.array([pixels * 4, pixels * 16])
        # Building the obstacle 105
        self.obstacle105 = self.canvas_widget.create_rectangle(
            obstacle105_center[0] - 10, obstacle105_center[1] - 10,  # Top left corner
            obstacle105_center[0] + 10, obstacle105_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 105 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle105 = [self.canvas_widget.coords(self.obstacle105)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle105)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle105)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle105)[3] - 3]

        # Obstacle 106
        # Defining the center of obstacle 106
        obstacle106_center = self.o + np.array([pixels * 5, pixels * 16])
        # Building the obstacle 106
        self.obstacle106 = self.canvas_widget.create_rectangle(
            obstacle106_center[0] - 10, obstacle106_center[1] - 10,  # Top left corner
            obstacle106_center[0] + 10, obstacle106_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 106 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle106 = [self.canvas_widget.coords(self.obstacle106)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle106)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle106)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle106)[3] - 3]

        # Obstacle 107
        # Defining the center of obstacle 107
        obstacle107_center = self.o + np.array([pixels * 2, pixels * 27])
        # Building the obstacle 107
        self.obstacle107 = self.canvas_widget.create_rectangle(
            obstacle107_center[0] - 10, obstacle107_center[1] - 10,  # Top left corner
            obstacle107_center[0] + 10, obstacle107_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 107 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle107 = [self.canvas_widget.coords(self.obstacle107)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle107)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle107)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle107)[3] - 3]

        # Obstacle 108
        # Defining the center of obstacle 108
        obstacle108_center = self.o + np.array([pixels * 2, pixels * 28])
        # Building the obstacle 108
        self.obstacle108 = self.canvas_widget.create_rectangle(
            obstacle108_center[0] - 10, obstacle108_center[1] - 10,  # Top left corner
            obstacle108_center[0] + 10, obstacle108_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 108 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle108 = [self.canvas_widget.coords(self.obstacle108)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle108)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle108)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle108)[3] - 3]

        # Obstacle 109
        # Defining the center of obstacle 109
        obstacle109_center = self.o + np.array([pixels * 3, pixels * 28])
        # Building the obstacle 109
        self.obstacle109 = self.canvas_widget.create_rectangle(
            obstacle109_center[0] - 10, obstacle109_center[1] - 10,  # Top left corner
            obstacle109_center[0] + 10, obstacle109_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 109 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle109 = [self.canvas_widget.coords(self.obstacle109)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle109)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle109)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle109)[3] - 3]

        # Obstacle 110
        # Defining the center of obstacle 110
        obstacle110_center = self.o + np.array([pixels * 4, pixels * 28])
        # Building the obstacle 110
        self.obstacle110 = self.canvas_widget.create_rectangle(
            obstacle110_center[0] - 10, obstacle110_center[1] - 10,  # Top left corner
            obstacle110_center[0] + 10, obstacle110_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 110 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle110 = [self.canvas_widget.coords(self.obstacle110)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle110)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle110)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle110)[3] - 3]

        # Obstacle 111
        # Defining the center of obstacle 111
        obstacle111_center = self.o + np.array([pixels * 5, pixels * 28])
        # Building the obstacle 111
        self.obstacle111 = self.canvas_widget.create_rectangle(
            obstacle111_center[0] - 10, obstacle111_center[1] - 10,  # Top left corner
            obstacle111_center[0] + 10, obstacle111_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 111 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle111 = [self.canvas_widget.coords(self.obstacle111)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle111)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle111)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle111)[3] - 3]

        # Obstacle 112
        # Defining the center of obstacle 112
        obstacle112_center = self.o + np.array([pixels * 6, pixels * 28])
        # Building the obstacle 112
        self.obstacle112 = self.canvas_widget.create_rectangle(
            obstacle112_center[0] - 10, obstacle112_center[1] - 10,  # Top left corner
            obstacle112_center[0] + 10, obstacle112_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 112 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle112 = [self.canvas_widget.coords(self.obstacle112)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle112)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle112)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle112)[3] - 3]

        # Obstacle 113
        # Defining the center of obstacle 113
        obstacle113_center = self.o + np.array([pixels * 7, pixels * 28])
        # Building the obstacle 113
        self.obstacle113 = self.canvas_widget.create_rectangle(
            obstacle113_center[0] - 10, obstacle113_center[1] - 10,  # Top left corner
            obstacle113_center[0] + 10, obstacle113_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 113 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle113 = [self.canvas_widget.coords(self.obstacle113)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle113)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle113)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle113)[3] - 3]

        # Obstacle 114
        # Defining the center of obstacle 114
        obstacle114_center = self.o + np.array([pixels * 7, pixels * 27])
        # Building the obstacle 114
        self.obstacle114 = self.canvas_widget.create_rectangle(
            obstacle114_center[0] - 10, obstacle114_center[1] - 10,  # Top left corner
            obstacle114_center[0] + 10, obstacle114_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 114 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle114 = [self.canvas_widget.coords(self.obstacle114)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle114)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle114)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle114)[3] - 3]

        # Obstacle 115
        # Defining the center of obstacle 115
        obstacle115_center = self.o + np.array([pixels * 7, pixels * 26])
        # Building the obstacle 115
        self.obstacle115 = self.canvas_widget.create_rectangle(
            obstacle115_center[0] - 10, obstacle115_center[1] - 10,  # Top left corner
            obstacle115_center[0] + 10, obstacle115_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 115 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle115 = [self.canvas_widget.coords(self.obstacle115)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle115)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle115)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle115)[3] - 3]

        # Obstacle 116
        # Defining the center of obstacle 116
        obstacle116_center = self.o + np.array([pixels * 7, pixels * 25])
        # Building the obstacle 116
        self.obstacle116 = self.canvas_widget.create_rectangle(
            obstacle116_center[0] - 10, obstacle116_center[1] - 10,  # Top left corner
            obstacle116_center[0] + 10, obstacle116_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 116 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle116 = [self.canvas_widget.coords(self.obstacle116)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle116)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle116)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle116)[3] - 3]

        # Obstacle 117
        # Defining the center of obstacle 117
        obstacle117_center = self.o + np.array([pixels * 7, pixels * 24])
        # Building the obstacle 117
        self.obstacle117 = self.canvas_widget.create_rectangle(
            obstacle117_center[0] - 10, obstacle117_center[1] - 10,  # Top left corner
            obstacle117_center[0] + 10, obstacle117_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 117 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle117 = [self.canvas_widget.coords(self.obstacle117)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle117)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle117)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle117)[3] - 3]

        # Obstacle 118
        # Defining the center of obstacle 118
        obstacle118_center = self.o + np.array([pixels * 9, pixels * 22])
        # Building the obstacle 118
        self.obstacle118 = self.canvas_widget.create_rectangle(
            obstacle118_center[0] - 10, obstacle118_center[1] - 10,  # Top left corner
            obstacle118_center[0] + 10, obstacle118_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 118 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle118 = [self.canvas_widget.coords(self.obstacle118)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle118)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle118)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle118)[3] - 3]

        # Obstacle 119
        # Defining the center of obstacle 119
        obstacle119_center = self.o + np.array([pixels * 9, pixels * 21])
        # Building the obstacle 119
        self.obstacle119 = self.canvas_widget.create_rectangle(
            obstacle119_center[0] - 10, obstacle119_center[1] - 10,  # Top left corner
            obstacle119_center[0] + 10, obstacle119_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 119 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle119 = [self.canvas_widget.coords(self.obstacle119)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle119)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle119)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle119)[3] - 3]

        # Obstacle 120
        # Defining the center of obstacle 120
        obstacle120_center = self.o + np.array([pixels * 9, pixels * 20])
        # Building the obstacle 120
        self.obstacle120 = self.canvas_widget.create_rectangle(
            obstacle120_center[0] - 10, obstacle120_center[1] - 10,  # Top left corner
            obstacle120_center[0] + 10, obstacle120_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 120 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle120 = [self.canvas_widget.coords(self.obstacle120)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle120)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle120)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle120)[3] - 3]

        # Obstacle 121
        # Defining the center of obstacle 121
        obstacle121_center = self.o + np.array([pixels * 9, pixels * 19])
        # Building the obstacle 121
        self.obstacle121 = self.canvas_widget.create_rectangle(
            obstacle121_center[0] - 10, obstacle121_center[1] - 10,  # Top left corner
            obstacle121_center[0] + 10, obstacle121_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 121 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle121 = [self.canvas_widget.coords(self.obstacle121)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle121)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle121)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle121)[3] - 3]

        # Obstacle 122
        # Defining the center of obstacle 122
        obstacle122_center = self.o + np.array([pixels * 9, pixels * 18])
        # Building the obstacle 122
        self.obstacle122 = self.canvas_widget.create_rectangle(
            obstacle122_center[0] - 10, obstacle122_center[1] - 10,  # Top left corner
            obstacle122_center[0] + 10, obstacle122_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 122 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle122 = [self.canvas_widget.coords(self.obstacle122)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle122)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle122)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle122)[3] - 3]

        # Obstacle 123
        # Defining the center of obstacle 123
        obstacle123_center = self.o + np.array([pixels * 8, pixels * 18])
        # Building the obstacle 123
        self.obstacle123 = self.canvas_widget.create_rectangle(
            obstacle123_center[0] - 10, obstacle123_center[1] - 10,  # Top left corner
            obstacle123_center[0] + 10, obstacle123_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 123 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle123 = [self.canvas_widget.coords(self.obstacle123)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle123)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle123)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle123)[3] - 3]

        # Obstacle 124
        # Defining the center of obstacle 124
        obstacle124_center = self.o + np.array([pixels * 7, pixels * 18])
        # Building the obstacle 124
        self.obstacle124 = self.canvas_widget.create_rectangle(
            obstacle124_center[0] - 10, obstacle124_center[1] - 10,  # Top left corner
            obstacle124_center[0] + 10, obstacle124_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 124 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle124 = [self.canvas_widget.coords(self.obstacle124)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle124)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle124)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle124)[3] - 3]

        # Obstacle 125
        # Defining the center of obstacle 125
        obstacle125_center = self.o + np.array([pixels * 7, pixels * 16])
        # Building the obstacle 125
        self.obstacle125 = self.canvas_widget.create_rectangle(
            obstacle125_center[0] - 10, obstacle125_center[1] - 10,  # Top left corner
            obstacle125_center[0] + 10, obstacle125_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 125 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle125 = [self.canvas_widget.coords(self.obstacle125)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle125)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle125)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle125)[3] - 3]

        # Obstacle 126
        # Defining the center of obstacle 126
        obstacle126_center = self.o + np.array([pixels * 7, pixels * 15])
        # Building the obstacle 126
        self.obstacle126 = self.canvas_widget.create_rectangle(
            obstacle126_center[0] - 10, obstacle126_center[1] - 10,  # Top left corner
            obstacle126_center[0] + 10, obstacle126_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 126 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle126 = [self.canvas_widget.coords(self.obstacle126)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle126)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle126)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle126)[3] - 3]

        # Obstacle 127
        # Defining the center of obstacle 127
        obstacle127_center = self.o + np.array([pixels * 7, pixels * 17])
        # Building the obstacle 127
        self.obstacle127 = self.canvas_widget.create_rectangle(
            obstacle127_center[0] - 10, obstacle127_center[1] - 10,  # Top left corner
            obstacle127_center[0] + 10, obstacle127_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 127 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle127 = [self.canvas_widget.coords(self.obstacle127)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle127)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle127)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle127)[3] - 3]

        # Obstacle 128
        # Defining the center of obstacle 128
        obstacle128_center = self.o + np.array([pixels * 8, pixels * 15])
        # Building the obstacle 128
        self.obstacle128 = self.canvas_widget.create_rectangle(
            obstacle128_center[0] - 10, obstacle128_center[1] - 10,  # Top left corner
            obstacle128_center[0] + 10, obstacle128_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 128 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle128 = [self.canvas_widget.coords(self.obstacle128)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle128)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle128)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle128)[3] - 3]

        # Obstacle 129
        # Defining the center of obstacle 129
        obstacle129_center = self.o + np.array([pixels * 9, pixels * 15])
        # Building the obstacle 129
        self.obstacle129 = self.canvas_widget.create_rectangle(
            obstacle129_center[0] - 10, obstacle129_center[1] - 10,  # Top left corner
            obstacle129_center[0] + 10, obstacle129_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 129 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle129 = [self.canvas_widget.coords(self.obstacle129)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle129)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle129)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle129)[3] - 3]

        # Obstacle 130
        # Defining the center of obstacle 130
        obstacle130_center = self.o + np.array([pixels * 10, pixels * 15])
        # Building the obstacle 130
        self.obstacle130 = self.canvas_widget.create_rectangle(
            obstacle130_center[0] - 10, obstacle130_center[1] - 10,  # Top left corner
            obstacle130_center[0] + 10, obstacle130_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 130 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle130 = [self.canvas_widget.coords(self.obstacle130)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle130)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle130)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle130)[3] - 3]

        # Obstacle 131
        # Defining the center of obstacle 131
        obstacle131_center = self.o + np.array([pixels * 11, pixels * 12])
        # Building the obstacle 131
        self.obstacle131 = self.canvas_widget.create_rectangle(
            obstacle131_center[0] - 10, obstacle131_center[1] - 10,  # Top left corner
            obstacle131_center[0] + 10, obstacle131_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 131 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle131 = [self.canvas_widget.coords(self.obstacle131)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle131)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle131)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle131)[3] - 3]

        # Obstacle 132
        # Defining the center of obstacle 132
        obstacle132_center = self.o + np.array([pixels * 10, pixels * 12])
        # Building the obstacle 132
        self.obstacle132 = self.canvas_widget.create_rectangle(
            obstacle132_center[0] - 10, obstacle132_center[1] - 10,  # Top left corner
            obstacle132_center[0] + 10, obstacle132_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 132 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle132 = [self.canvas_widget.coords(self.obstacle132)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle132)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle132)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle132)[3] - 3]

        # Obstacle 133
        # Defining the center of obstacle 133
        obstacle133_center = self.o + np.array([pixels * 11, pixels * 13])
        # Building the obstacle 133
        self.obstacle133 = self.canvas_widget.create_rectangle(
            obstacle133_center[0] - 10, obstacle133_center[1] - 10,  # Top left corner
            obstacle133_center[0] + 10, obstacle133_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 133 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle133 = [self.canvas_widget.coords(self.obstacle133)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle133)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle133)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle133)[3] - 3]

        # Obstacle 134
        # Defining the center of obstacle 134
        obstacle134_center = self.o + np.array([pixels * 12, pixels * 13])
        # Building the obstacle 134
        self.obstacle134 = self.canvas_widget.create_rectangle(
            obstacle134_center[0] - 10, obstacle134_center[1] - 10,  # Top left corner
            obstacle134_center[0] + 10, obstacle134_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 134 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle134 = [self.canvas_widget.coords(self.obstacle134)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle134)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle134)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle134)[3] - 3]

        # Obstacle 135
        # Defining the center of obstacle 135
        obstacle135_center = self.o + np.array([pixels * 13, pixels * 13])
        # Building the obstacle 135
        self.obstacle135 = self.canvas_widget.create_rectangle(
            obstacle135_center[0] - 10, obstacle135_center[1] - 10,  # Top left corner
            obstacle135_center[0] + 10, obstacle135_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 135 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle135 = [self.canvas_widget.coords(self.obstacle135)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle135)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle135)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle135)[3] - 3]

        # Obstacle 136
        # Defining the center of obstacle 136
        obstacle136_center = self.o + np.array([pixels * 13, pixels * 14])
        # Building the obstacle 136
        self.obstacle136 = self.canvas_widget.create_rectangle(
            obstacle136_center[0] - 10, obstacle136_center[1] - 10,  # Top left corner
            obstacle136_center[0] + 10, obstacle136_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 136 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle136 = [self.canvas_widget.coords(self.obstacle136)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle136)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle136)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle136)[3] - 3]

        # Obstacle 137
        # Defining the center of obstacle 137
        obstacle137_center = self.o + np.array([pixels * 13, pixels * 15])
        # Building the obstacle 137
        self.obstacle137 = self.canvas_widget.create_rectangle(
            obstacle137_center[0] - 10, obstacle137_center[1] - 10,  # Top left corner
            obstacle137_center[0] + 10, obstacle137_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 137 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle137 = [self.canvas_widget.coords(self.obstacle137)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle137)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle137)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle137)[3] - 3]

        # Obstacle 138
        # Defining the center of obstacle 138
        obstacle138_center = self.o + np.array([pixels * 14, pixels * 15])
        # Building the obstacle 138
        self.obstacle138 = self.canvas_widget.create_rectangle(
            obstacle138_center[0] - 10, obstacle138_center[1] - 10,  # Top left corner
            obstacle138_center[0] + 10, obstacle138_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 138 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle138 = [self.canvas_widget.coords(self.obstacle138)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle138)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle138)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle138)[3] - 3]

        # Obstacle 139
        # Defining the center of obstacle 139
        obstacle139_center = self.o + np.array([pixels * 15, pixels * 15])
        # Building the obstacle 139
        self.obstacle139 = self.canvas_widget.create_rectangle(
            obstacle139_center[0] - 10, obstacle139_center[1] - 10,  # Top left corner
            obstacle139_center[0] + 10, obstacle139_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 139 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle139 = [self.canvas_widget.coords(self.obstacle139)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle139)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle139)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle139)[3] - 3]

        # Obstacle 140
        # Defining the center of obstacle 140
        obstacle140_center = self.o + np.array([pixels * 16, pixels * 15])
        # Building the obstacle 140
        self.obstacle140 = self.canvas_widget.create_rectangle(
            obstacle140_center[0] - 10, obstacle140_center[1] - 10,  # Top left corner
            obstacle140_center[0] + 10, obstacle140_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 140 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle140 = [self.canvas_widget.coords(self.obstacle140)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle140)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle140)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle140)[3] - 3]

        # Obstacle 141
        # Defining the center of obstacle 141
        obstacle141_center = self.o + np.array([pixels * 17, pixels * 15])
        # Building the obstacle 141
        self.obstacle141 = self.canvas_widget.create_rectangle(
            obstacle141_center[0] - 10, obstacle141_center[1] - 10,  # Top left corner
            obstacle141_center[0] + 10, obstacle141_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 141 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle141 = [self.canvas_widget.coords(self.obstacle141)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle141)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle141)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle141)[3] - 3]

        # Obstacle 142
        # Defining the center of obstacle 142
        obstacle142_center = self.o + np.array([pixels * 18, pixels * 15])
        # Building the obstacle 142
        self.obstacle142 = self.canvas_widget.create_rectangle(
            obstacle142_center[0] - 10, obstacle142_center[1] - 10,  # Top left corner
            obstacle142_center[0] + 10, obstacle142_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 142 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle142 = [self.canvas_widget.coords(self.obstacle142)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle142)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle142)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle142)[3] - 3]

        # Obstacle 143
        # Defining the center of obstacle 143
        obstacle143_center = self.o + np.array([pixels * 18, pixels * 14])
        # Building the obstacle 143
        self.obstacle143 = self.canvas_widget.create_rectangle(
            obstacle143_center[0] - 10, obstacle143_center[1] - 10,  # Top left corner
            obstacle143_center[0] + 10, obstacle143_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 143 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle143 = [self.canvas_widget.coords(self.obstacle143)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle143)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle143)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle143)[3] - 3]

        # Obstacle 144
        # Defining the center of obstacle 144
        obstacle144_center = self.o + np.array([pixels * 18, pixels * 13])
        # Building the obstacle 144
        self.obstacle144 = self.canvas_widget.create_rectangle(
            obstacle144_center[0] - 10, obstacle144_center[1] - 10,  # Top left corner
            obstacle144_center[0] + 10, obstacle144_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 144 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle144 = [self.canvas_widget.coords(self.obstacle144)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle144)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle144)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle144)[3] - 3]

        # Obstacle 145
        # Defining the center of obstacle 145
        obstacle145_center = self.o + np.array([pixels * 15, pixels * 17])
        # Building the obstacle 145
        self.obstacle145 = self.canvas_widget.create_rectangle(
            obstacle145_center[0] - 10, obstacle145_center[1] - 10,  # Top left corner
            obstacle145_center[0] + 10, obstacle145_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 145 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle145 = [self.canvas_widget.coords(self.obstacle145)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle145)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle145)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle145)[3] - 3]

        # Obstacle 146
        # Defining the center of obstacle 146
        obstacle146_center = self.o + np.array([pixels * 14, pixels * 17])
        # Building the obstacle 146
        self.obstacle146 = self.canvas_widget.create_rectangle(
            obstacle146_center[0] - 10, obstacle146_center[1] - 10,  # Top left corner
            obstacle146_center[0] + 10, obstacle146_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 146 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle146 = [self.canvas_widget.coords(self.obstacle146)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle146)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle146)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle146)[3] - 3]

        # Obstacle 147
        # Defining the center of obstacle 147
        obstacle147_center = self.o + np.array([pixels * 13, pixels * 17])
        # Building the obstacle 147
        self.obstacle147 = self.canvas_widget.create_rectangle(
            obstacle147_center[0] - 10, obstacle147_center[1] - 10,  # Top left corner
            obstacle147_center[0] + 10, obstacle147_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 147 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle147 = [self.canvas_widget.coords(self.obstacle147)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle147)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle147)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle147)[3] - 3]

        # Obstacle 148
        # Defining the center of obstacle 148
        obstacle148_center = self.o + np.array([pixels * 12, pixels * 17])
        # Building the obstacle 148
        self.obstacle148 = self.canvas_widget.create_rectangle(
            obstacle148_center[0] - 10, obstacle148_center[1] - 10,  # Top left corner
            obstacle148_center[0] + 10, obstacle148_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 148 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle148 = [self.canvas_widget.coords(self.obstacle148)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle148)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle148)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle148)[3] - 3]

        # Obstacle 149
        # Defining the center of obstacle 149
        obstacle149_center = self.o + np.array([pixels * 12, pixels * 18])
        # Building the obstacle 149
        self.obstacle149 = self.canvas_widget.create_rectangle(
            obstacle149_center[0] - 10, obstacle149_center[1] - 10,  # Top left corner
            obstacle149_center[0] + 10, obstacle149_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 149 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle149 = [self.canvas_widget.coords(self.obstacle149)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle149)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle149)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle149)[3] - 3]

        # Obstacle 150
        # Defining the center of obstacle 150
        obstacle150_center = self.o + np.array([pixels * 12, pixels * 19])
        # Building the obstacle 150
        self.obstacle150 = self.canvas_widget.create_rectangle(
            obstacle150_center[0] - 10, obstacle150_center[1] - 10,  # Top left corner
            obstacle150_center[0] + 10, obstacle150_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 150 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle150 = [self.canvas_widget.coords(self.obstacle150)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle150)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle150)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle150)[3] - 3]

        # Obstacle 151
        # Defining the center of obstacle 151
        obstacle151_center = self.o + np.array([pixels * 12, pixels * 20])
        # Building the obstacle 151
        self.obstacle151 = self.canvas_widget.create_rectangle(
            obstacle151_center[0] - 10, obstacle151_center[1] - 10,  # Top left corner
            obstacle151_center[0] + 10, obstacle151_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 151 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle151 = [self.canvas_widget.coords(self.obstacle151)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle151)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle151)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle151)[3] - 3]

        # Obstacle 152
        # Defining the center of obstacle 152
        obstacle152_center = self.o + np.array([pixels * 12, pixels * 21])
        # Building the obstacle 152
        self.obstacle152 = self.canvas_widget.create_rectangle(
            obstacle152_center[0] - 10, obstacle152_center[1] - 10,  # Top left corner
            obstacle152_center[0] + 10, obstacle152_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 152 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle152 = [self.canvas_widget.coords(self.obstacle152)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle152)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle152)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle152)[3] - 3]

        # Obstacle 153
        # Defining the center of obstacle 153
        obstacle153_center = self.o + np.array([pixels * 12, pixels * 22])
        # Building the obstacle 153
        self.obstacle153 = self.canvas_widget.create_rectangle(
            obstacle153_center[0] - 10, obstacle153_center[1] - 10,  # Top left corner
            obstacle153_center[0] + 10, obstacle153_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 153 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle153 = [self.canvas_widget.coords(self.obstacle153)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle153)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle153)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle153)[3] - 3]

        # Obstacle 154
        # Defining the center of obstacle 154
        obstacle154_center = self.o + np.array([pixels * 12, pixels * 23])
        # Building the obstacle 154
        self.obstacle154 = self.canvas_widget.create_rectangle(
            obstacle154_center[0] - 10, obstacle154_center[1] - 10,  # Top left corner
            obstacle154_center[0] + 10, obstacle154_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 154 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle154 = [self.canvas_widget.coords(self.obstacle154)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle154)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle154)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle154)[3] - 3]

        # Obstacle 155
        # Defining the center of obstacle 155
        obstacle155_center = self.o + np.array([pixels * 12, pixels * 24])
        # Building the obstacle 155
        self.obstacle155 = self.canvas_widget.create_rectangle(
            obstacle155_center[0] - 10, obstacle155_center[1] - 10,  # Top left corner
            obstacle155_center[0] + 10, obstacle155_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 155 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle155 = [self.canvas_widget.coords(self.obstacle155)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle155)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle155)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle155)[3] - 3]

        # Obstacle 156
        # Defining the center of obstacle 156
        obstacle156_center = self.o + np.array([pixels * 12, pixels * 25])
        # Building the obstacle 156
        self.obstacle156 = self.canvas_widget.create_rectangle(
            obstacle156_center[0] - 10, obstacle156_center[1] - 10,  # Top left corner
            obstacle156_center[0] + 10, obstacle156_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 156 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle156 = [self.canvas_widget.coords(self.obstacle156)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle156)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle156)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle156)[3] - 3]

        # Obstacle 157
        # Defining the center of obstacle 157
        obstacle157_center = self.o + np.array([pixels * 11, pixels * 25])
        # Building the obstacle 157
        self.obstacle157 = self.canvas_widget.create_rectangle(
            obstacle157_center[0] - 10, obstacle157_center[1] - 10,  # Top left corner
            obstacle157_center[0] + 10, obstacle157_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 157 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle157 = [self.canvas_widget.coords(self.obstacle157)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle157)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle157)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle157)[3] - 3]

        # Obstacle 158
        # Defining the center of obstacle 158
        obstacle158_center = self.o + np.array([pixels * 10, pixels * 25])
        # Building the obstacle 158
        self.obstacle158 = self.canvas_widget.create_rectangle(
            obstacle158_center[0] - 10, obstacle158_center[1] - 10,  # Top left corner
            obstacle158_center[0] + 10, obstacle158_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 158 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle158 = [self.canvas_widget.coords(self.obstacle158)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle158)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle158)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle158)[3] - 3]

        # Obstacle 159
        # Defining the center of obstacle 159
        obstacle159_center = self.o + np.array([pixels * 9, pixels * 25])
        # Building the obstacle 159
        self.obstacle159 = self.canvas_widget.create_rectangle(
            obstacle159_center[0] - 10, obstacle159_center[1] - 10,  # Top left corner
            obstacle159_center[0] + 10, obstacle159_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 159 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle159 = [self.canvas_widget.coords(self.obstacle159)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle159)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle159)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle159)[3] - 3]

        # Obstacle 160
        # Defining the center of obstacle 160
        obstacle160_center = self.o + np.array([pixels * 21, pixels * 27])
        # Building the obstacle 160
        self.obstacle160 = self.canvas_widget.create_rectangle(
            obstacle160_center[0] - 10, obstacle160_center[1] - 10,  # Top left corner
            obstacle160_center[0] + 10, obstacle160_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 160 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle160 = [self.canvas_widget.coords(self.obstacle160)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle160)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle160)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle160)[3] - 3]

        # Obstacle 161
        # Defining the center of obstacle 161
        obstacle161_center = self.o + np.array([pixels * 10, pixels * 28])
        # Building the obstacle 161
        self.obstacle161 = self.canvas_widget.create_rectangle(
            obstacle161_center[0] - 10, obstacle161_center[1] - 10,  # Top left corner
            obstacle161_center[0] + 10, obstacle161_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 161 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle161 = [self.canvas_widget.coords(self.obstacle161)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle161)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle161)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle161)[3] - 3]

        # Obstacle 162
        # Defining the center of obstacle 162
        obstacle162_center = self.o + np.array([pixels * 10, pixels * 27])
        # Building the obstacle 162
        self.obstacle162 = self.canvas_widget.create_rectangle(
            obstacle162_center[0] - 10, obstacle162_center[1] - 10,  # Top left corner
            obstacle162_center[0] + 10, obstacle162_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 162 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle162 = [self.canvas_widget.coords(self.obstacle162)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle162)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle162)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle162)[3] - 3]

        # Obstacle 163
        # Defining the center of obstacle 163
        obstacle163_center = self.o + np.array([pixels * 11, pixels * 27])
        # Building the obstacle 163
        self.obstacle163 = self.canvas_widget.create_rectangle(
            obstacle163_center[0] - 10, obstacle163_center[1] - 10,  # Top left corner
            obstacle163_center[0] + 10, obstacle163_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 163 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle163 = [self.canvas_widget.coords(self.obstacle163)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle163)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle163)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle163)[3] - 3]

        # Obstacle 164
        # Defining the center of obstacle 164
        obstacle164_center = self.o + np.array([pixels * 12, pixels * 27])
        # Building the obstacle 164
        self.obstacle164 = self.canvas_widget.create_rectangle(
            obstacle164_center[0] - 10, obstacle164_center[1] - 10,  # Top left corner
            obstacle164_center[0] + 10, obstacle164_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 164 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle164 = [self.canvas_widget.coords(self.obstacle164)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle164)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle164)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle164)[3] - 3]

        # Obstacle 165
        # Defining the center of obstacle 165
        obstacle165_center = self.o + np.array([pixels * 13, pixels * 27])
        # Building the obstacle 165
        self.obstacle165 = self.canvas_widget.create_rectangle(
            obstacle165_center[0] - 10, obstacle165_center[1] - 10,  # Top left corner
            obstacle165_center[0] + 10, obstacle165_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 165 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle165 = [self.canvas_widget.coords(self.obstacle165)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle165)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle165)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle165)[3] - 3]

        # Obstacle 166
        # Defining the center of obstacle 166
        obstacle166_center = self.o + np.array([pixels * 14, pixels * 27])
        # Building the obstacle 166
        self.obstacle166 = self.canvas_widget.create_rectangle(
            obstacle166_center[0] - 10, obstacle166_center[1] - 10,  # Top left corner
            obstacle166_center[0] + 10, obstacle166_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 166 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle166 = [self.canvas_widget.coords(self.obstacle166)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle166)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle166)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle166)[3] - 3]

        # Obstacle 167
        # Defining the center of obstacle 167
        obstacle167_center = self.o + np.array([pixels * 15, pixels * 27])
        # Building the obstacle 167
        self.obstacle167 = self.canvas_widget.create_rectangle(
            obstacle167_center[0] - 10, obstacle167_center[1] - 10,  # Top left corner
            obstacle167_center[0] + 10, obstacle167_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 167 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle167 = [self.canvas_widget.coords(self.obstacle167)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle167)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle167)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle167)[3] - 3]

        # Obstacle 168
        # Defining the center of obstacle 168
        obstacle168_center = self.o + np.array([pixels * 16, pixels * 27])
        # Building the obstacle 168
        self.obstacle168 = self.canvas_widget.create_rectangle(
            obstacle168_center[0] - 10, obstacle168_center[1] - 10,  # Top left corner
            obstacle168_center[0] + 10, obstacle168_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 168 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle168 = [self.canvas_widget.coords(self.obstacle168)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle168)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle168)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle168)[3] - 3]

        # Obstacle 169
        # Defining the center of obstacle 169
        obstacle169_center = self.o + np.array([pixels * 16, pixels * 28])
        # Building the obstacle 169
        self.obstacle169 = self.canvas_widget.create_rectangle(
            obstacle169_center[0] - 10, obstacle169_center[1] - 10,  # Top left corner
            obstacle169_center[0] + 10, obstacle169_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 169 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle169 = [self.canvas_widget.coords(self.obstacle169)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle169)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle169)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle169)[3] - 3]

        # Obstacle 170
        # Defining the center of obstacle 170
        obstacle170_center = self.o + np.array([pixels * 14, pixels * 24])
        # Building the obstacle 170
        self.obstacle170 = self.canvas_widget.create_rectangle(
            obstacle170_center[0] - 10, obstacle170_center[1] - 10,  # Top left corner
            obstacle170_center[0] + 10, obstacle170_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 170 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle170 = [self.canvas_widget.coords(self.obstacle170)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle170)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle170)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle170)[3] - 3]

        # Obstacle 171
        # Defining the center of obstacle 171
        obstacle171_center = self.o + np.array([pixels * 15, pixels * 24])
        # Building the obstacle 171
        self.obstacle171 = self.canvas_widget.create_rectangle(
            obstacle171_center[0] - 10, obstacle171_center[1] - 10,  # Top left corner
            obstacle171_center[0] + 10, obstacle171_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 171 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle171 = [self.canvas_widget.coords(self.obstacle171)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle171)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle171)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle171)[3] - 3]

        # Obstacle 172
        # Defining the center of obstacle 172
        obstacle172_center = self.o + np.array([pixels * 16, pixels * 24])
        # Building the obstacle 172
        self.obstacle172 = self.canvas_widget.create_rectangle(
            obstacle172_center[0] - 10, obstacle172_center[1] - 10,  # Top left corner
            obstacle172_center[0] + 10, obstacle172_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 172 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle172 = [self.canvas_widget.coords(self.obstacle172)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle172)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle172)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle172)[3] - 3]

        # Obstacle 173
        # Defining the center of obstacle 173
        obstacle173_center = self.o + np.array([pixels * 17, pixels * 24])
        # Building the obstacle 173
        self.obstacle173 = self.canvas_widget.create_rectangle(
            obstacle173_center[0] - 10, obstacle173_center[1] - 10,  # Top left corner
            obstacle173_center[0] + 10, obstacle173_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 173 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle173 = [self.canvas_widget.coords(self.obstacle173)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle173)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle173)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle173)[3] - 3]

        # Obstacle 174
        # Defining the center of obstacle 174
        obstacle174_center = self.o + np.array([pixels * 17, pixels * 23])
        # Building the obstacle 174
        self.obstacle174 = self.canvas_widget.create_rectangle(
            obstacle174_center[0] - 10, obstacle174_center[1] - 10,  # Top left corner
            obstacle174_center[0] + 10, obstacle174_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 174 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle174 = [self.canvas_widget.coords(self.obstacle174)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle174)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle174)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle174)[3] - 3]

        # Obstacle 175
        # Defining the center of obstacle 175
        obstacle175_center = self.o + np.array([pixels * 17, pixels * 22])
        # Building the obstacle 175
        self.obstacle175 = self.canvas_widget.create_rectangle(
            obstacle175_center[0] - 10, obstacle175_center[1] - 10,  # Top left corner
            obstacle175_center[0] + 10, obstacle175_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 175 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle175 = [self.canvas_widget.coords(self.obstacle175)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle175)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle175)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle175)[3] - 3]

        # Obstacle 176
        # Defining the center of obstacle 176
        obstacle176_center = self.o + np.array([pixels * 17, pixels * 21])
        # Building the obstacle 176
        self.obstacle176 = self.canvas_widget.create_rectangle(
            obstacle176_center[0] - 10, obstacle176_center[1] - 10,  # Top left corner
            obstacle176_center[0] + 10, obstacle176_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 176 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle176 = [self.canvas_widget.coords(self.obstacle176)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle176)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle176)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle176)[3] - 3]

        # Obstacle 177
        # Defining the center of obstacle 177
        obstacle177_center = self.o + np.array([pixels * 17, pixels * 20])
        # Building the obstacle 177
        self.obstacle177 = self.canvas_widget.create_rectangle(
            obstacle177_center[0] - 10, obstacle177_center[1] - 10,  # Top left corner
            obstacle177_center[0] + 10, obstacle177_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 177 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle177 = [self.canvas_widget.coords(self.obstacle177)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle177)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle177)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle177)[3] - 3]

        # Obstacle 178
        # Defining the center of obstacle 178
        obstacle178_center = self.o + np.array([pixels * 17, pixels * 19])
        # Building the obstacle 178
        self.obstacle178 = self.canvas_widget.create_rectangle(
            obstacle178_center[0] - 10, obstacle178_center[1] - 10,  # Top left corner
            obstacle178_center[0] + 10, obstacle178_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 178 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle178 = [self.canvas_widget.coords(self.obstacle178)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle178)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle178)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle178)[3] - 3]

        # Obstacle 179
        # Defining the center of obstacle 179
        obstacle179_center = self.o + np.array([pixels * 17, pixels * 18])
        # Building the obstacle 179
        self.obstacle179 = self.canvas_widget.create_rectangle(
            obstacle179_center[0] - 10, obstacle179_center[1] - 10,  # Top left corner
            obstacle179_center[0] + 10, obstacle179_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 179 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle179 = [self.canvas_widget.coords(self.obstacle179)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle179)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle179)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle179)[3] - 3]

        # Obstacle 180
        # Defining the center of obstacle 180
        obstacle180_center = self.o + np.array([pixels * 18, pixels * 18])
        # Building the obstacle 180
        self.obstacle180 = self.canvas_widget.create_rectangle(
            obstacle180_center[0] - 10, obstacle180_center[1] - 10,  # Top left corner
            obstacle180_center[0] + 10, obstacle180_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 180 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle180 = [self.canvas_widget.coords(self.obstacle180)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle180)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle180)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle180)[3] - 3]

        # Obstacle 181
        # Defining the center of obstacle 181
        obstacle181_center = self.o + np.array([pixels * 19, pixels * 18])
        # Building the obstacle 181
        self.obstacle181 = self.canvas_widget.create_rectangle(
            obstacle181_center[0] - 10, obstacle181_center[1] - 10,  # Top left corner
            obstacle181_center[0] + 10, obstacle181_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 181 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle181 = [self.canvas_widget.coords(self.obstacle181)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle181)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle181)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle181)[3] - 3]

        # Obstacle 182
        # Defining the center of obstacle 182
        obstacle182_center = self.o + np.array([pixels * 20, pixels * 18])
        # Building the obstacle 182
        self.obstacle182 = self.canvas_widget.create_rectangle(
            obstacle182_center[0] - 10, obstacle182_center[1] - 10,  # Top left corner
            obstacle182_center[0] + 10, obstacle182_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 182 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle182 = [self.canvas_widget.coords(self.obstacle182)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle182)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle182)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle182)[3] - 3]

        # Obstacle 183
        # Defining the center of obstacle 183
        obstacle183_center = self.o + np.array([pixels * 21, pixels * 18])
        # Building the obstacle 183
        self.obstacle183 = self.canvas_widget.create_rectangle(
            obstacle183_center[0] - 10, obstacle183_center[1] - 10,  # Top left corner
            obstacle183_center[0] + 10, obstacle183_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 183 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle183 = [self.canvas_widget.coords(self.obstacle183)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle183)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle183)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle183)[3] - 3]

        # Obstacle 184
        # Defining the center of obstacle 184
        obstacle184_center = self.o + np.array([pixels * 22, pixels * 18])
        # Building the obstacle 184
        self.obstacle184 = self.canvas_widget.create_rectangle(
            obstacle184_center[0] - 10, obstacle184_center[1] - 10,  # Top left corner
            obstacle184_center[0] + 10, obstacle184_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 184 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle184 = [self.canvas_widget.coords(self.obstacle184)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle184)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle184)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle184)[3] - 3]

        # Obstacle 185
        # Defining the center of obstacle 185
        obstacle185_center = self.o + np.array([pixels * 23, pixels * 18])
        # Building the obstacle 185
        self.obstacle185 = self.canvas_widget.create_rectangle(
            obstacle185_center[0] - 10, obstacle185_center[1] - 10,  # Top left corner
            obstacle185_center[0] + 10, obstacle185_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 185 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle185 = [self.canvas_widget.coords(self.obstacle185)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle185)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle185)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle185)[3] - 3]

        # Obstacle 186
        # Defining the center of obstacle 186
        obstacle186_center = self.o + np.array([pixels * 23, pixels * 18])
        # Building the obstacle 186
        self.obstacle186 = self.canvas_widget.create_rectangle(
            obstacle186_center[0] - 10, obstacle186_center[1] - 10,  # Top left corner
            obstacle186_center[0] + 10, obstacle186_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 186 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle186 = [self.canvas_widget.coords(self.obstacle186)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle186)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle186)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle186)[3] - 3]

        # Obstacle 187
        # Defining the center of obstacle 187
        obstacle187_center = self.o + np.array([pixels * 23, pixels * 19])
        # Building the obstacle 187
        self.obstacle187 = self.canvas_widget.create_rectangle(
            obstacle187_center[0] - 10, obstacle187_center[1] - 10,  # Top left corner
            obstacle187_center[0] + 10, obstacle187_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 187 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle187 = [self.canvas_widget.coords(self.obstacle187)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle187)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle187)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle187)[3] - 3]

        # Obstacle 188
        # Defining the center of obstacle 188
        obstacle188_center = self.o + np.array([pixels * 23, pixels * 20])
        # Building the obstacle 188
        self.obstacle188 = self.canvas_widget.create_rectangle(
            obstacle188_center[0] - 10, obstacle188_center[1] - 10,  # Top left corner
            obstacle188_center[0] + 10, obstacle188_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 188 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle188 = [self.canvas_widget.coords(self.obstacle188)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle188)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle188)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle188)[3] - 3]

        # Obstacle 189
        # Defining the center of obstacle 189
        obstacle189_center = self.o + np.array([pixels * 23, pixels * 21])
        # Building the obstacle 189
        self.obstacle189 = self.canvas_widget.create_rectangle(
            obstacle189_center[0] - 10, obstacle189_center[1] - 10,  # Top left corner
            obstacle189_center[0] + 10, obstacle189_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 189 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle189 = [self.canvas_widget.coords(self.obstacle189)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle189)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle189)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle189)[3] - 3]

        # Obstacle 190
        # Defining the center of obstacle 190
        obstacle190_center = self.o + np.array([pixels * 23, pixels * 22])
        # Building the obstacle 190
        self.obstacle190 = self.canvas_widget.create_rectangle(
            obstacle190_center[0] - 10, obstacle190_center[1] - 10,  # Top left corner
            obstacle190_center[0] + 10, obstacle190_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 190 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle190 = [self.canvas_widget.coords(self.obstacle190)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle190)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle190)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle190)[3] - 3]

        # Obstacle 191
        # Defining the center of obstacle 191
        obstacle191_center = self.o + np.array([pixels * 23, pixels * 23])
        # Building the obstacle 191
        self.obstacle191 = self.canvas_widget.create_rectangle(
            obstacle191_center[0] - 10, obstacle191_center[1] - 10,  # Top left corner
            obstacle191_center[0] + 10, obstacle191_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 191 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle191 = [self.canvas_widget.coords(self.obstacle191)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle191)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle191)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle191)[3] - 3]

        # Obstacle 192
        # Defining the center of obstacle 192
        obstacle192_center = self.o + np.array([pixels * 23, pixels * 24])
        # Building the obstacle 192
        self.obstacle192 = self.canvas_widget.create_rectangle(
            obstacle192_center[0] - 10, obstacle192_center[1] - 10,  # Top left corner
            obstacle192_center[0] + 10, obstacle192_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 192 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle192 = [self.canvas_widget.coords(self.obstacle192)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle192)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle192)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle192)[3] - 3]

        # Obstacle 193
        # Defining the center of obstacle 193
        obstacle193_center = self.o + np.array([pixels * 23, pixels * 25])
        # Building the obstacle 193
        self.obstacle193 = self.canvas_widget.create_rectangle(
            obstacle193_center[0] - 10, obstacle193_center[1] - 10,  # Top left corner
            obstacle193_center[0] + 10, obstacle193_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 193 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle193 = [self.canvas_widget.coords(self.obstacle193)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle193)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle193)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle193)[3] - 3]

        # Obstacle 194
        # Defining the center of obstacle 194
        obstacle194_center = self.o + np.array([pixels * 23, pixels * 26])
        # Building the obstacle 194
        self.obstacle194 = self.canvas_widget.create_rectangle(
            obstacle194_center[0] - 10, obstacle194_center[1] - 10,  # Top left corner
            obstacle194_center[0] + 10, obstacle194_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 194 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle194 = [self.canvas_widget.coords(self.obstacle194)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle194)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle194)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle194)[3] - 3]

        # Obstacle 195
        # Defining the center of obstacle 195
        obstacle195_center = self.o + np.array([pixels * 23, pixels * 27])
        # Building the obstacle 195
        self.obstacle195 = self.canvas_widget.create_rectangle(
            obstacle195_center[0] - 10, obstacle195_center[1] - 10,  # Top left corner
            obstacle195_center[0] + 10, obstacle195_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 195 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle195 = [self.canvas_widget.coords(self.obstacle195)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle195)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle195)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle195)[3] - 3]

        # Obstacle 196
        # Defining the center of obstacle 196
        obstacle196_center = self.o + np.array([pixels * 22, pixels * 27])
        # Building the obstacle 196
        self.obstacle196 = self.canvas_widget.create_rectangle(
            obstacle196_center[0] - 10, obstacle196_center[1] - 10,  # Top left corner
            obstacle196_center[0] + 10, obstacle196_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 196 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle196 = [self.canvas_widget.coords(self.obstacle196)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle196)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle196)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle196)[3] - 3]

        # Obstacle 197
        # Defining the center of obstacle 197
        obstacle197_center = self.o + np.array([pixels * 21, pixels * 16])
        # Building the obstacle 197
        self.obstacle197 = self.canvas_widget.create_rectangle(
            obstacle197_center[0] - 10, obstacle197_center[1] - 10,  # Top left corner
            obstacle197_center[0] + 10, obstacle197_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 197 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle197 = [self.canvas_widget.coords(self.obstacle197)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle197)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle197)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle197)[3] - 3]

        # Obstacle 198
        # Defining the center of obstacle 198
        obstacle198_center = self.o + np.array([pixels * 22, pixels * 16])
        # Building the obstacle 198
        self.obstacle198 = self.canvas_widget.create_rectangle(
            obstacle198_center[0] - 10, obstacle198_center[1] - 10,  # Top left corner
            obstacle198_center[0] + 10, obstacle198_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 198 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle198 = [self.canvas_widget.coords(self.obstacle198)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle198)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle198)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle198)[3] - 3]

        # Obstacle 199
        # Defining the center of obstacle 199
        obstacle199_center = self.o + np.array([pixels * 23, pixels * 16])
        # Building the obstacle 199
        self.obstacle199 = self.canvas_widget.create_rectangle(
            obstacle199_center[0] - 10, obstacle199_center[1] - 10,  # Top left corner
            obstacle199_center[0] + 10, obstacle199_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 199 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle199 = [self.canvas_widget.coords(self.obstacle199)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle199)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle199)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle199)[3] - 3]

        # Obstacle 200
        # Defining the center of obstacle 200
        obstacle200_center = self.o + np.array([pixels * 24, pixels * 16])
        # Building the obstacle 200
        self.obstacle200 = self.canvas_widget.create_rectangle(
            obstacle200_center[0] - 10, obstacle200_center[1] - 10,  # Top left corner
            obstacle200_center[0] + 10, obstacle200_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 200 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle200 = [self.canvas_widget.coords(self.obstacle200)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle200)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle200)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle200)[3] - 3]

        # Obstacle 201
        # Defining the center of obstacle 201
        obstacle201_center = self.o + np.array([pixels * 25, pixels * 16])
        # Building the obstacle 201
        self.obstacle201 = self.canvas_widget.create_rectangle(
            obstacle201_center[0] - 10, obstacle201_center[1] - 10,  # Top left corner
            obstacle201_center[0] + 10, obstacle201_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 201 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle201 = [self.canvas_widget.coords(self.obstacle201)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle201)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle201)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle201)[3] - 3]

        # Obstacle 202
        # Defining the center of obstacle 202
        obstacle202_center = self.o + np.array([pixels * 26, pixels * 17])
        # Building the obstacle 202
        self.obstacle202 = self.canvas_widget.create_rectangle(
            obstacle202_center[0] - 10, obstacle202_center[1] - 10,  # Top left corner
            obstacle202_center[0] + 10, obstacle202_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 202 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle202 = [self.canvas_widget.coords(self.obstacle202)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle202)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle202)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle202)[3] - 3]

        # Obstacle 203
        # Defining the center of obstacle 203
        obstacle203_center = self.o + np.array([pixels * 26, pixels * 16])
        # Building the obstacle 203
        self.obstacle203 = self.canvas_widget.create_rectangle(
            obstacle203_center[0] - 10, obstacle203_center[1] - 10,  # Top left corner
            obstacle203_center[0] + 10, obstacle203_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 203 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle203 = [self.canvas_widget.coords(self.obstacle203)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle203)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle203)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle203)[3] - 3]

        # Obstacle 204
        # Defining the center of obstacle 204
        obstacle204_center = self.o + np.array([pixels * 26, pixels * 18])
        # Building the obstacle 204
        self.obstacle204 = self.canvas_widget.create_rectangle(
            obstacle204_center[0] - 10, obstacle204_center[1] - 10,  # Top left corner
            obstacle204_center[0] + 10, obstacle204_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 204 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle204 = [self.canvas_widget.coords(self.obstacle204)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle204)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle204)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle204)[3] - 3]

        # Obstacle 205
        # Defining the center of obstacle 205
        obstacle205_center = self.o + np.array([pixels * 27, pixels * 18])
        # Building the obstacle 205
        self.obstacle205 = self.canvas_widget.create_rectangle(
            obstacle205_center[0] - 10, obstacle205_center[1] - 10,  # Top left corner
            obstacle205_center[0] + 10, obstacle205_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 205 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle205 = [self.canvas_widget.coords(self.obstacle205)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle205)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle205)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle205)[3] - 3]

        # Obstacle 206
        # Defining the center of obstacle 206
        obstacle206_center = self.o + np.array([pixels * 28, pixels * 18])
        # Building the obstacle 206
        self.obstacle206 = self.canvas_widget.create_rectangle(
            obstacle206_center[0] - 10, obstacle206_center[1] - 10,  # Top left corner
            obstacle206_center[0] + 10, obstacle206_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 206 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle206 = [self.canvas_widget.coords(self.obstacle206)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle206)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle206)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle206)[3] - 3]

        # Obstacle 207
        # Defining the center of obstacle 207
        obstacle207_center = self.o + np.array([pixels * 27, pixels * 27])
        # Building the obstacle 207
        self.obstacle207 = self.canvas_widget.create_rectangle(
            obstacle207_center[0] - 10, obstacle207_center[1] - 10,  # Top left corner
            obstacle207_center[0] + 10, obstacle207_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 207 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle207 = [self.canvas_widget.coords(self.obstacle207)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle207)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle207)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle207)[3] - 3]

        # Obstacle 208
        # Defining the center of obstacle 208
        obstacle208_center = self.o + np.array([pixels * 28, pixels * 27])
        # Building the obstacle 208
        self.obstacle208 = self.canvas_widget.create_rectangle(
            obstacle208_center[0] - 10, obstacle208_center[1] - 10,  # Top left corner
            obstacle208_center[0] + 10, obstacle208_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 208 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle208 = [self.canvas_widget.coords(self.obstacle208)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle208)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle208)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle208)[3] - 3]

        # Obstacle 209
        # Defining the center of obstacle 209
        obstacle209_center = self.o + np.array([pixels * 28, pixels * 26])
        # Building the obstacle 209
        self.obstacle209 = self.canvas_widget.create_rectangle(
            obstacle209_center[0] - 10, obstacle209_center[1] - 10,  # Top left corner
            obstacle209_center[0] + 10, obstacle209_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 209 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle209 = [self.canvas_widget.coords(self.obstacle209)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle209)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle209)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle209)[3] - 3]

        # Obstacle 210
        # Defining the center of obstacle 210
        obstacle210_center = self.o + np.array([pixels * 28, pixels * 25])
        # Building the obstacle 210
        self.obstacle210 = self.canvas_widget.create_rectangle(
            obstacle210_center[0] - 10, obstacle210_center[1] - 10,  # Top left corner
            obstacle210_center[0] + 10, obstacle210_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 210 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle210 = [self.canvas_widget.coords(self.obstacle210)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle210)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle210)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle210)[3] - 3]

        # Obstacle 211
        # Defining the center of obstacle 211
        obstacle211_center = self.o + np.array([pixels * 28, pixels * 24])
        # Building the obstacle 211
        self.obstacle211 = self.canvas_widget.create_rectangle(
            obstacle211_center[0] - 10, obstacle211_center[1] - 10,  # Top left corner
            obstacle211_center[0] + 10, obstacle211_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 211 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle211 = [self.canvas_widget.coords(self.obstacle211)[0] + 3,
                                  self.canvas_widget.coords(self.obstacle211)[1] + 3,
                                  self.canvas_widget.coords(self.obstacle211)[2] - 3,
                                  self.canvas_widget.coords(self.obstacle211)[3] - 3]

        # Obstacle 212
        # Defining the center of obstacle 212
        obstacle212_center = self.o + np.array([pixels * 27, pixels * 24])
        # Building the obstacle 212
        self.obstacle212 = self.canvas_widget.create_rectangle(
            obstacle212_center[0] - 10, obstacle212_center[1] - 10,  # Top left corner
            obstacle212_center[0] + 10, obstacle212_center[1] + 10,  # Bottom right corner
            outline='grey', fill='#00BFFF')
        # Saving the coordinates of obstacle 212 according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_obstacle212 = [self.canvas_widget.coords(self.obstacle212)[0] + 3,
                                   self.canvas_widget.coords(self.obstacle212)[1] + 3,
                                   self.canvas_widget.coords(self.obstacle212)[2] - 3,
                                   self.canvas_widget.coords(self.obstacle212)[3] - 3]

        # Creating an agent of Mobile Robot - red point
        self.agent = self.canvas_widget.create_oval(
            self.o[0] - 7, self.o[1] - 7,
            self.o[0] + 7, self.o[1] + 7,
            outline='#FF1493', fill='#FF1493')

        # Final Point - yellow point
        flag_center = self.o + np.array([pixels * 20, pixels * 20])
        # Building the flag
        self.flag = self.canvas_widget.create_rectangle(
            flag_center[0] - 10, flag_center[1] - 10,  # Top left corner
            flag_center[0] + 10, flag_center[1] + 10,  # Bottom right corner
            outline='grey', fill='yellow')
        # Saving the coordinates of the final point according to the size of agent
        # In order to fit the coordinates of the agent
        self.coords_flag = [self.canvas_widget.coords(self.flag)[0] + 3,
                            self.canvas_widget.coords(self.flag)[1] + 3,
                            self.canvas_widget.coords(self.flag)[2] - 3,
                            self.canvas_widget.coords(self.flag)[3] - 3]

        # Packing everything
        self.canvas_widget.pack()

    # Function to reset the environment and start new Episode
    def reset(self):
        self.update()
        #time.sleep(0.5)

        # Updating agent
        self.canvas_widget.delete(self.agent)
        self.agent = self.canvas_widget.create_oval(
            self.o[0] - 7, self.o[1] - 7,
            self.o[0] + 7, self.o[1] + 7,
            outline='red', fill='red')

        # Clearing the dictionary and the i
        self.d = {}
        self.i = 0

        # Return observation
        return self.canvas_widget.coords(self.agent)

    # Function to get the next observation and reward by doing next step
    def step(self, action):
        # Current state of the agent
        state = self.canvas_widget.coords(self.agent)
        base_action = np.array([0, 0])

        # Updating next state according to the action
        # Action 'up'
        if action == 0:
            if state[1] >= pixels:
                base_action[1] -= pixels
        # Action 'down'
        elif action == 1:
            if state[1] < (env_height - 1) * pixels:
                base_action[1] += pixels
        # Action right
        elif action == 2:
            if state[0] < (env_width - 1) * pixels:
                base_action[0] += pixels
        # Action left
        elif action == 3:
            if state[0] >= pixels:
                base_action[0] -= pixels

        # Moving the agent according to the action
        self.canvas_widget.move(self.agent, base_action[0], base_action[1])

        # Writing in the dictionary coordinates of found route
        self.d[self.i] = self.canvas_widget.coords(self.agent)

        # Updating next state
        next_state = self.d[self.i]

        # Updating key for the dictionary
        self.i += 1

        # Calculating the reward for the agent
        if next_state == self.coords_flag:
            time.sleep(0.1)
            reward = 1
            done = True
            next_state = 'goal'

            # Filling the dictionary first time
            if self.c == True:
                for j in range(len(self.d)):
                    self.f[j] = self.d[j]
                self.c = False
                self.longest = len(self.d)
                self.shortest = len(self.d)

            # Checking if the currently found route is shorter
            if len(self.d) < len(self.f):
                # Saving the number of steps for the shortest route
                self.shortest = len(self.d)
                # Clearing the dictionary for the final route
                self.f = {}
                # Reassigning the dictionary
                for j in range(len(self.d)):
                    self.f[j] = self.d[j]

            # Saving the number of steps for the longest route
            if len(self.d) > self.longest:
                self.longest = len(self.d)

        elif next_state in [self.coords_obstacle1,
                            self.coords_obstacle2,
                            self.coords_obstacle3,
                            self.coords_obstacle4,
                            self.coords_obstacle5,
                            self.coords_obstacle6,
                            self.coords_obstacle7,
                            self.coords_obstacle8,
                            self.coords_obstacle9,
                            self.coords_obstacle10,
                            self.coords_obstacle11,
                            self.coords_obstacle12,
                            self.coords_obstacle13,
                            self.coords_obstacle14,
                            self.coords_obstacle15,
                            self.coords_obstacle16,
                            self.coords_obstacle17,
                            self.coords_obstacle18,
                            self.coords_obstacle19,
                            self.coords_obstacle20,
                            self.coords_obstacle21,
                            self.coords_obstacle22,
                            self.coords_obstacle23,
                            self.coords_obstacle24,
                            self.coords_obstacle25,
                            self.coords_obstacle26,
                            self.coords_obstacle27,
                            self.coords_obstacle28,
                            self.coords_obstacle29,
                            self.coords_obstacle30,
                            self.coords_obstacle31,
                            self.coords_obstacle32,
                            self.coords_obstacle33,
                            self.coords_obstacle34,
                            self.coords_obstacle35,
                            self.coords_obstacle36,
                            self.coords_obstacle37,
                            self.coords_obstacle38,
                            self.coords_obstacle39,
                            self.coords_obstacle40,
                            self.coords_obstacle41,
                            self.coords_obstacle42,
                            self.coords_obstacle43,
                            self.coords_obstacle44,
                            self.coords_obstacle45,
                            self.coords_obstacle46,
                            self.coords_obstacle47,
                            self.coords_obstacle48,
                            self.coords_obstacle49,
                            self.coords_obstacle50,
                            self.coords_obstacle51,
                            self.coords_obstacle52,
                            self.coords_obstacle53,
                            self.coords_obstacle54,
                            self.coords_obstacle55,
                            self.coords_obstacle56,
                            self.coords_obstacle57,
                            self.coords_obstacle58,
                            self.coords_obstacle59,
                            self.coords_obstacle60,
                            self.coords_obstacle61,
                            self.coords_obstacle62,
                            self.coords_obstacle63,
                            self.coords_obstacle64,
                            self.coords_obstacle65,
                            self.coords_obstacle66,
                            self.coords_obstacle66,
                            self.coords_obstacle67,
                            self.coords_obstacle68,
                            self.coords_obstacle69,
                            self.coords_obstacle70,
                            self.coords_obstacle71,
                            self.coords_obstacle72,
                            self.coords_obstacle73,
                            self.coords_obstacle74,
                            self.coords_obstacle75,
                            self.coords_obstacle76,
                            self.coords_obstacle77,
                            self.coords_obstacle78,
                            self.coords_obstacle79,
                            self.coords_obstacle80,
                            self.coords_obstacle81,
                            self.coords_obstacle82,
                            self.coords_obstacle83,
                            self.coords_obstacle84,
                            self.coords_obstacle85,
                            self.coords_obstacle86,
                            self.coords_obstacle87,
                            self.coords_obstacle88,
                            self.coords_obstacle89,
                            self.coords_obstacle90,
                            self.coords_obstacle91,
                            self.coords_obstacle92,
                            self.coords_obstacle93,
                            self.coords_obstacle94,
                            self.coords_obstacle95,
                            self.coords_obstacle96,
                            self.coords_obstacle97,
                            self.coords_obstacle98,
                            self.coords_obstacle99,
                            self.coords_obstacle100,
                            self.coords_obstacle101,
                            self.coords_obstacle102,
                            self.coords_obstacle103,
                            self.coords_obstacle104,
                            self.coords_obstacle105,
                            self.coords_obstacle106,
                            self.coords_obstacle107,
                            self.coords_obstacle108,
                            self.coords_obstacle109,
                            self.coords_obstacle110,
                            self.coords_obstacle111,
                            self.coords_obstacle112,
                            self.coords_obstacle113,
                            self.coords_obstacle114,
                            self.coords_obstacle115,
                            self.coords_obstacle116,
                            self.coords_obstacle117,
                            self.coords_obstacle118,
                            self.coords_obstacle119,
                            self.coords_obstacle120,
                            self.coords_obstacle121,
                            self.coords_obstacle122,
                            self.coords_obstacle123,
                            self.coords_obstacle124,
                            self.coords_obstacle125,
                            self.coords_obstacle126,
                            self.coords_obstacle127,
                            self.coords_obstacle128,
                            self.coords_obstacle129,
                            self.coords_obstacle130,
                            self.coords_obstacle131,
                            self.coords_obstacle132,
                            self.coords_obstacle133,
                            self.coords_obstacle134,
                            self.coords_obstacle135,
                            self.coords_obstacle136,
                            self.coords_obstacle137,
                            self.coords_obstacle138,
                            self.coords_obstacle139,
                            self.coords_obstacle140,
                            self.coords_obstacle141,
                            self.coords_obstacle142,
                            self.coords_obstacle143,
                            self.coords_obstacle144,
                            self.coords_obstacle145,
                            self.coords_obstacle146,
                            self.coords_obstacle147,
                            self.coords_obstacle148,
                            self.coords_obstacle149,
                            self.coords_obstacle150,
                            self.coords_obstacle151,
                            self.coords_obstacle152,
                            self.coords_obstacle153,
                            self.coords_obstacle154,
                            self.coords_obstacle155,
                            self.coords_obstacle156,
                            self.coords_obstacle157,
                            self.coords_obstacle158,
                            self.coords_obstacle159,
                            self.coords_obstacle160,
                            self.coords_obstacle161,
                            self.coords_obstacle162,
                            self.coords_obstacle163,
                            self.coords_obstacle164,
                            self.coords_obstacle165,
                            self.coords_obstacle166,
                            self.coords_obstacle167,
                            self.coords_obstacle168,
                            self.coords_obstacle169,
                            self.coords_obstacle170,
                            self.coords_obstacle171,
                            self.coords_obstacle172,
                            self.coords_obstacle173,
                            self.coords_obstacle174,
                            self.coords_obstacle175,
                            self.coords_obstacle176,
                            self.coords_obstacle177,
                            self.coords_obstacle178,
                            self.coords_obstacle179,
                            self.coords_obstacle180,
                            self.coords_obstacle181,
                            self.coords_obstacle182,
                            self.coords_obstacle183,
                            self.coords_obstacle184,
                            self.coords_obstacle185,
                            self.coords_obstacle186,
                            self.coords_obstacle187,
                            self.coords_obstacle188,
                            self.coords_obstacle189,
                            self.coords_obstacle190,
                            self.coords_obstacle191,
                            self.coords_obstacle192,
                            self.coords_obstacle193,
                            self.coords_obstacle194,
                            self.coords_obstacle195,
                            self.coords_obstacle196,
                            self.coords_obstacle197,
                            self.coords_obstacle198,
                            self.coords_obstacle199,
                            self.coords_obstacle200,
                            self.coords_obstacle201,
                            self.coords_obstacle202,
                            self.coords_obstacle203,
                            self.coords_obstacle204,
                            self.coords_obstacle205,
                            self.coords_obstacle206,
                            self.coords_obstacle207,
                            self.coords_obstacle208,
                            self.coords_obstacle209,
                            self.coords_obstacle210,
                            self.coords_obstacle211,
                            self.coords_obstacle212]:

            reward = -1
            done = True
            next_state = 'obstacle'

            # Clearing the dictionary and the i
            self.d = {}
            self.i = 0

        else:
            reward = 0
            done = False

        return next_state, reward, done

    # Function to refresh the environment
    def render(self):
        #time.sleep(0.03)
        self.update()

    # Function to show the found route
    def final(self):
        # Deleting the agent at the end
        self.canvas_widget.delete(self.agent)

        # Showing the number of steps
        print('The shortest route:', self.shortest)
        print('The longest route:', self.longest)

        # Creating initial point
        self.initial_point = self.canvas_widget.create_oval(
            self.o[0] - 4, self.o[1] - 4,
            self.o[0] + 4, self.o[1] + 4,
            fill='blue', outline='blue')

        # Filling the route
        for j in range(len(self.f)):
            # Showing the coordinates of the final route
            print(self.f[j])
            self.track = self.canvas_widget.create_oval(
                self.f[j][0] - 3 + self.o[0] - 4, self.f[j][1] - 3 + self.o[1] - 4,
                self.f[j][0] - 3 + self.o[0] + 4, self.f[j][1] - 3 + self.o[1] + 4,
                fill='blue', outline='blue')
            # Writing the final route in the global variable a
            a[j] = self.f[j]


# Returning the final dictionary with route coordinates
# Then it will be used in agent_brain.py
def final_states():
    return a


# This we need to debug the environment
# If we want to run and see the environment without running full algorithm
if __name__ == '__main__':
    env = Environment()
    env.mainloop()
