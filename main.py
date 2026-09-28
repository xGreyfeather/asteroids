import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

	pygame.init()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	clock = pygame.time.Clock()
	dt = 0.0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroidfield = AsteroidField()

	while True:

		log_state()

		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				return

		screen.fill("black")

		for each in drawable:
			each.draw(screen)

		updatable.update(dt)

		for each in asteroids:
			if each.collides_with(player) == True:
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for each_shot in shots:
				if each_shot.collides_with(each) == True:
					log_event("asteroid_shot")
					each.split()
					each_shot.kill()

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
