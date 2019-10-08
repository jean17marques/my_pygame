#!bin/bash/python3
#######################################################
#   config - main configuration file 
#                    
#
#   author  : the kid 
#   version : 0.0.1
#   date    : oct 2019
#
########################################################
import pygame
from pygame.locals import *

import eventhandler as eh

class GameObject():
    def __init__(self, ID, attrs):
        
        self.ID = ID
        
        for key, value in attrs.items():
            setattr(self, key, value)
        
        self.rect = pygame.rect.Rect(self.pos, self.size)
        self.rect.center = self.pos

    def update_rect_pos(self):
        self.rect.center = self.pos
    
    def update_pos(self, x, y):
        self.pos = x, y
        self.update_rect_pos()

    def tofu_blit(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Player(GameObject):

    def __init__(self, ID, attrs):
        super().__init__(ID, attrs)

        self.move_tag = 'i'

    @eh.player_move_event.listen_event
    def move(self, time, move_func=lambda s, t: s*t):
        
        x, y = self.pos

        if self.move_tag == 'ru':
            x += move_func(self.speed, time)
            y -= move_func(self.speed, time)
        elif self.move_tag == 'rd':
            x += move_func(self.speed, time)
            y += move_func(self.speed, time)
        elif self.move_tag == 'lu':
            x -= move_func(self.speed, time)
            y -= move_func(self.speed, time)
        elif self.move_tag == 'ld':
            x -= move_func(self.speed, time)
            y += move_func(self.speed, time)
        elif self.move_tag == 'r':
            x += move_func(self.speed, time)
        elif self.move_tag == 'l':
            x -= move_func(self.speed, time)
        elif self.move_tag == 'u':
            y -= move_func(self.speed, time)
        elif self.move_tag == 'd':
            y += move_func(self.speed, time)
        
        self.move_tag = 'i'
        self.update_pos(x, y) 

    @eh.player_move_event.listen_condition
    def move_condition(self):
        token = True
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and keys[K_UP]:
            self.move_tag = 'ru'
        elif keys[K_RIGHT] and keys[K_DOWN]:
            self.move_tag = 'rd'
        elif keys[K_LEFT] and keys[K_UP]:
            self.move_tag = 'lu'
        elif keys[K_LEFT] and keys[K_DOWN]:
            self.move_tag = 'ld'
        elif keys[K_RIGHT]:
            self.move_tag = 'r'
        elif keys[K_LEFT]:
            self.move_tag = 'l'
        elif keys[K_UP]:
            self.move_tag = 'u'
        elif keys[K_DOWN]:
            self.move_tag = 'd'
        else:
            self.move_tag = 'i'
            token = False
        
        return token 

    def run(self, surface, time, move_func=lambda s, t: s*t):
        self.move_condition()
        self.move(time, move_func)
        self.tofu_blit(surface)
        
        










