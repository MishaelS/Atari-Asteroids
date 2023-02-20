from constants import *
from vector2   import Vector2

import pygame
import math

# ---------------------------------------------------------------------------

class Ship:
	def __init__(self):
	# --- private --- #
		self.__position = Vector2((WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
		self.__velocity = Vector2((0, 0))
		self.__radius = 16

		self.__speed_move = 0.1
		self.__speed_rotate = 4
		self.__angle_rotate = 0
		self.__friction_force = 0.98

	def set_rotation_angle(self, angle):
		self.__angle_rotate += angle

	def changing_angle(self, dist, angle):
		func = lambda angle: angle*math.pi/ONE_PI
		if self.__angle_rotate > 360 or self.__angle_rotate < -360:
			self.__angle_rotate = 0

		pos_x = dist*math.sin(-func(self.__angle_rotate + angle + 90)) + self.__position.x
		pos_y = dist*math.cos(-func(self.__angle_rotate + angle + 90)) + self.__position.y
		return [pos_x, pos_y]

	def placement_points(self):
		points = []
		for key in POINTS_ANGLE:
			point = self.changing_angle(self.__radius/POINTS_ANGLE[key], key)
			points.append(point)
		return points

	def management(self, keys):
		if keys[pygame.K_a]:
			self.set_rotation_angle(-self.__speed_rotate)
		if keys[pygame.K_d]:
			self.set_rotation_angle(self.__speed_rotate)
		if keys[pygame.K_w]:
			self.boost(self.__speed_move)
		if keys[pygame.K_s]:
			self.boost(-self.__speed_move)

	def boost(self, speed):
		force = Vector2( self.changing_angle(self.__radius/1, ONE_PI) )
		force.Vdetermine_direction(self.__position)
		force.normalize()
		force.mult(speed)
		self.__velocity.Vadd(force)

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
		self.__velocity.mult(self.__friction_force)

	def update(self):
		keys = pygame.key.get_pressed()

		self.set_rotation_angle(0)
		self.management(keys)
		self.movement()
		self.borders()

	def draw(self, surface):
		pygame.draw.lines(surface, WHITE, True, self.placement_points(), 1)