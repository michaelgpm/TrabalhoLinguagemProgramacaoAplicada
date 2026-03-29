#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
            case 'Player':
                return Player('Player', (WIN_WIDTH / 2, 200))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_HEIGHT + 10, random.randint(0, WIN_WIDTH)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_HEIGHT + 20, random.randint(0, WIN_WIDTH)))
