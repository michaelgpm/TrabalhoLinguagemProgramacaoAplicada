#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centery += 1
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(0, WIN_WIDTH)
