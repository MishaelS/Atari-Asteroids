from constants import *
from ship      import Ship
from asteroid  import Asteroid

import pygame
import sys

pygame.init()

# ---------------------------------------------------------------------------

class Game:
	def __init__(self):
		pygame.display.set_caption(TITLE)
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()

		self.ship = Ship()
		self.asteroids = [Asteroid() for _ in range(5)]

	def run(self):
		while True:
			self.window.fill(BLACK)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.ship.update()
			self.ship.draw(self.window)

			for asteroid in self.asteroids:
				asteroid.update()
				asteroid.draw(self.window)

			pygame.display.flip()
			self.clock.tick(FRAMERATE)

# ---------------------------------------------------------------------------

if __name__ == '__main__':
	game = Game()
	game.run()