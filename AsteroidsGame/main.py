import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteriodfield import *
from shot import Shot
from logger import log_event
import sys

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_over = False
    clock = pygame.time.Clock()
    dt = 0
    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteriod_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while game_over == False:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
