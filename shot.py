import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.direction = direction

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.direction)
        self.position += forward * self.velocity * dt