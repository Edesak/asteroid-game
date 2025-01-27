import pygame 
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from player import Player
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return 20
        else:
            angle = random.uniform(20,50)
            v1,v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_r)
            a2 = Asteroid(self.position.x, self.position.y, new_r)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
            self.kill()
            return 10