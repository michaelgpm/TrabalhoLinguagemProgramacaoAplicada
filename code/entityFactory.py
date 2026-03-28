#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_HEIGHT
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
