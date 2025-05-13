import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, position, velocity, radius):
        if isinstance(position, pygame.Vector2):
            super().__init__(position.x, position.y, radius)
        elif isinstance(position, (list, tuple)) and len(position) >= 2:
            super().__init__(position[0], position[1], radius)

        else:
            super().__init__(position, velocity, radius)
        if not isinstance(velocity, pygame.Vector2):
            self.velocity = pygame.Vector2(velocity)
        else:
            self.velocity = velocity
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        dir1 = self.velocity.rotate(random_angle)
        dir2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position, dir1 * 1.2, new_radius)
        asteroid2 = Asteroid(self.position, dir2 * 1.2, new_radius)

        for container in Asteroid.containers:
            container.add(asteroid1, asteroid2)

       