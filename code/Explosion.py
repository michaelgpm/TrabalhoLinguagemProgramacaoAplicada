from code.entity import Entity


class Explosion(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.timer = 10  # frames the explosion lasts

    def move(self):
        self.timer -= 1
        if self.timer <= 0:
            return True  # remove explosion