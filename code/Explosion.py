import pygame
from code.entity import Entity

class Explosion(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.timer = 10  # lasts 10 frames
        self.surf = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, (255, 150, 0), (20, 20), 20)  # simple orange circle

    def move(self):
        self.timer -= 1
        if self.timer <= 0:
            return True  # mark for removal