from constants import *
from random    import *
from vector2   import Vector2

import pygame
import math

# ---------------------------------------------------------------------------

class Asteroid:
	def __init__(self):
	# --- private --- #
		self.__position = Vector2(( randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) ))
		self.__velocity = Vector2((uniform(-1, 1), uniform(-1, 1)))

		self.__number_points = randint(5, 10)
		self.__radius = randint(15, 50)
		self.__offset = [randint(-15, 15) for _ in range(self.__number_points)]

	def changing_angle(self, dist, angle):
		func = lambda angle: angle*math.pi/ONE_PI
		pos_x = dist*math.sin(func(angle + ONE_SECOND_PI)) + self.__position.x
		pos_y = dist*math.cos(func(angle + ONE_SECOND_PI)) + self.__position.y
		return [pos_x, pos_y]

	def placement_points(self):
		points = []
		for i in range(self.__number_points):
			dist = self.__radius + self.__offset[i]
			point = self.changing_angle(dist, i*(TWO_PI/self.__number_points))
			points.append(point)
		return points

	def borders(self):
		if self.__position.x < -self.__radius:
			self.__position.x = WINDOW_WIDTH + self.__radius
		elif self.__position.x > WINDOW_WIDTH + self.__radius:
			self.__position.x = -self.__radius

		if self.__position.y < -self.__radius:
			self.__position.y = WINDOW_HEIGHT + self.__radius
		elif self.__position.y > WINDOW_HEIGHT + self.__radius:
			self.__position.y = -self.__radius

	def movement(self):
		self.__position.Vadd(self.__velocity)

	def update(self):
		self.movement()
		self.borders()

	def draw(self, surface):
		pygame.draw.lines(surface, WHITE, True, self.placement_points(), 1)