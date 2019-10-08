#!bin/bash/python3
#######################################################
#   eventhandler - handles all game events and sets 
#                    responses
#
#   author  : the kid 
#   version : 0.0.1
#   date    : oct 2019
#
########################################################


import pygame 
from pygame.locals import *

#locals import 
import config

class Event():

    def __init__(self, event):
        self.event = event
        self.token = False

    def listen_condition(self, cond):
        def wrap_cond(*args, **kwargs):

            self.token = cond(*args, **kwargs)
            return self.token 

        wrap_cond.__name__ = cond.__name__
        return wrap_cond    

    def listen_event(self, func):

        def wrap_func(*args, **kwargs):
            if self.token:
                return func(*args, **kwargs) #runs and returns function
        
        #changes wrap function name 
        wrap_func.__name__ = func.__name__
        return wrap_func #returns wrap fucntion

    
PLAYER_MOVE_EVENT = USEREVENT + 1
player_move_event = Event(
    pygame.event.Event(PLAYER_MOVE_EVENT)
)

















