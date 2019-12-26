# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:03:32 2019

@author: majit
"""

import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time

style.use("ggplot")

SIZE = 10
HM_EPISODES = 25000
MOVE_PENALTY = 1  # feel free to tinker with these!
ENEMY_PENALTY = 300  # feel free to tinker with these!
FOOD_REWARD = 25  # feel free to tinker with these!
epsilon = 0.5  # randomness
EPS_DECAY = 0.9999  # Every episode will be epsilon*EPS_DECAY
SHOW_EVERY = 1000  # how often to play through env visually.

start_q_table = None  # if we have a pickled Q table, we'll put the filename of it here.

LEARNING_RATE = 0.1
DISCOUNT = 0.95

PLAYER_N = 1  # player key in dict
FOOD_N = 2  # food key in dict
ENEMY_N = 3  # enemy key in dict

# the dict! Using just for colors
d = {1: (255, 175, 0),  # blueish color
	 2: (0, 255, 0),  # green
	 3: (0, 0, 255)}  # red

class Blob:
	def __init__(self):
		self.x = np.random.randint(0, SIZE)
		self.y = np.random.randint(0, SIZE)

	def __str__(self):
		return f"{self.x}, {self.y}"

	def __sub__(self,other):
		return (self.x-other.x - self.y-other.y)
	
	def action(self, choice):
			'''
			Gives us 4 total movement options. (0,1,2,3)
			'''
			if choice == 0:
				self.move(x=1, y=1)
			elif choice == 1:
				self.move(x=-1, y=-1)
			elif choice == 2:
				self.move(x=-1, y=1)
			elif choice == 3:
				self.move(x=1, y=-1)


	def move(self,x = False,y = False):
		 # If no value for x, move randomly
		if not x:
			self.x += np.random.randint(-1, 2)
		else:
			self.x += x        

		if not y:
			self.y += np.random.randint(-1, 2)
		else:
			self.y += y


		# If we are out of bounds, fix!
		if self.x < 0:
			self.x = 0
		elif self.x > SIZE-1:
			self.x = SIZE-1
		if self.y < 0:
			self.y = 0
		elif self.y > SIZE-1:
			self.y = SIZE-1



player = Blob()
food = Blob()
enemy = Blob()

print(player)
print(food)
print(player-food)


