import pygame 
from pygame.locals import *

import sys 
from pprint import pprint
import random
#local import
import config
from config import conf 

import eventhandler as eh
import gamelib

"""
event_1 = eh.Event(
    pygame.event.Event(pygame.USEREVENT + 1)
)
@event_1.listen_condition
def test_cond(hello):
    return True

@event_1.listen_event
def test_action(foo):
    print(foo)
"""

def main():
    ######test##########
    pprint(config.conf.__dict__)
    ##########################

    screen = pygame.display.set_mode(conf.SCREEN_SIZE)

    clock = pygame.time.Clock()
    total_time = 0

    player = gamelib.Player(
        'player', conf.PLAYER_ATTRS
    )

    game_over = False
    while not game_over:

        time = clock.tick(conf.FPS) 
        total_time += time

        for event in pygame.event.get():
            #reads all events and dumps event qeue
            if event.type == pygame.QUIT:
                game_over = True

        #test_cond(5)
        #test_action('test ok')

        screen.fill(conf.SCREEN_COLOR)
        
        player.run(screen, time)

        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit(0)