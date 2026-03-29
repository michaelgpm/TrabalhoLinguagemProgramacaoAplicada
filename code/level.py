#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.time import Clock

from code import entity
from code.Const import EVENT_ENEMY, SPAWN_TIME, MAX_ENEMIES
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(240)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemies = [e for e in self.entity_list if isinstance(e, Enemy)]
                    if len(enemies) < MAX_ENEMIES:
                        enemy_type = random.choice(['Enemy1', 'Enemy2'])
                        self.entity_list.append(EntityFactory.get_entity(enemy_type))

            pygame.display.flip()
            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass
