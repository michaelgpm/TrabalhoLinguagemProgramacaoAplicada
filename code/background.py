#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity

class Background(Entity):
    def __init__(self,name:str, position: tuple):
        super().__init__(name,position)
        pass

    def move(self, ):
       self.y += self.speed
       self.rect.y = int(self.y)

       height = -self.surf.get_height()

       if self.rect.top >=339:
           assert isinstance(height, object)
           self.y=height
