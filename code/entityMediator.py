#!/usr/bin/python
# -*- coding: utf-8 -*-
from code import entity
from code.Const import WIN_HEIGHT
from code.enemy import Enemy
from code.playerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: entity):
        if isinstance(ent,Enemy):
            if ent.rect.bottom < 0:
                ent.health = 0
        if isinstance(ent,PlayerShot):
            if ent.rect.top >= WIN_HEIGHT:
                ent.health = 0



    @staticmethod
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
