# File: env.py
# Description: Building the environment-2 for the Mobile Robot to explore
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
env_height = 25  # grid height
env_width = 25  # grid width

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
        obstacle5_center = self.o + np.array([pixels * 4, pixels * 10])
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
        obstacle6_center = self.o + np.array([pixels * 4, pixels * 11])
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
        obstacle7_center = self.o + np.array([pixels * 4, pixels * 12])
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
        obstacle8_center = self.o + np.array([pixels * 5, pixels * 12])
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
        obstacle9_center = self.o + np.array([pixels * 6, pixels * 12])
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
        obstacle10_center = self.o + np.array([pixels * 2, pixels * 18])
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
        obstacle11_center = self.o + np.array([pixels * 3, pixels * 18])
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
        obstacle12_center = self.o + np.array([pixels * 4, pixels * 18])
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
        obstacle13_center = self.o + np.array([pixels * 3, pixels * 19])
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
        obstacle14_center = self.o + np.array([pixels * 3, pixels * 20])
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
        obstacle15_center = self.o + np.array([pixels * 3, pixels * 21])
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
        obstacle16_center = self.o + np.array([pixels * 10, pixels * 22])
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
        obstacle17_center = self.o + np.array([pixels * 11, pixels * 15])
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
        obstacle18_center = self.o + np.array([pixels * 12, pixels * 15])
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
        obstacle19_center = self.o + np.array([pixels * 13, pixels * 15])
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
        obstacle20_center = self.o + np.array([pixels * 13, pixels * 14])
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
        obstacle21_center = self.o + np.array([pixels * 13, pixels * 13])
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
        obstacle22_center = self.o + np.array([pixels * 21, pixels * 22])
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
        obstacle23_center = self.o + np.array([pixels * 20, pixels * 22])
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
        obstacle24_center = self.o + np.array([pixels * 19, pixels * 22])
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
        obstacle25_center = self.o + np.array([pixels * 18, pixels * 22])
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
        obstacle26_center = self.o + np.array([pixels * 18, pixels * 21])
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
        obstacle27_center = self.o + np.array([pixels * 18, pixels * 20])
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
        obstacle28_center = self.o + np.array([pixels * 18, pixels * 19])
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
        obstacle29_center = self.o + np.array([pixels * 18, pixels * 18])
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
        obstacle30_center = self.o + np.array([pixels * 19, pixels * 18])
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
        obstacle31_center = self.o + np.array([pixels * 20, pixels * 18])
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
        obstacle32_center = self.o + np.array([pixels * 11, pixels * 6])
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
        obstacle33_center = self.o + np.array([pixels * 12, pixels * 6])
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
        obstacle34_center = self.o + np.array([pixels * 13, pixels * 6])
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
        obstacle35_center = self.o + np.array([pixels * 14, pixels * 6])
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
        obstacle36_center = self.o + np.array([pixels * 14, pixels * 7])
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
        obstacle37_center = self.o + np.array([pixels * 14, pixels * 5])
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
        obstacle38_center = self.o + np.array([pixels * 20, pixels])
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
        obstacle39_center = self.o + np.array([pixels * 20, pixels * 2])
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
        obstacle40_center = self.o + np.array([pixels * 20, pixels * 3])
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
        obstacle41_center = self.o + np.array([pixels * 20, pixels * 4])
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
        obstacle42_center = self.o + np.array([pixels * 21, pixels * 4])
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
        obstacle43_center = self.o + np.array([pixels * 19, pixels * 4])
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
        obstacle44_center = self.o + np.array([pixels * 17, pixels * 10])
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
        obstacle45_center = self.o + np.array([pixels * 18, pixels * 10])
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
        obstacle46_center = self.o + np.array([pixels * 19, pixels * 10])
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
        obstacle47_center = self.o + np.array([pixels * 19, pixels * 9])
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
        obstacle48_center = self.o + np.array([pixels * 19, pixels * 8])
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
        obstacle49_center = self.o + np.array([pixels * 11, pixels * 23])
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
        obstacle50_center = self.o + np.array([pixels * 10, pixels * 23])
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
                            self.coords_obstacle50]:

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
