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

import os
import filehandler
import argparse

class Config():

    def __init__(self, config_path):
        """Configuration class
            path : configurantion file path (json)
        """
        ######## path to configuration file #########
        self.config_path = config_path

        ###### argparse attributes ######
        self.verbose = False

        self.load_json_config(self.config_path)
        self.argparse()

    
    def argparse(self):
        """parse argumnets from terminal"""
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--verbose', \
            help='displays more outputs', action='store_true')
        parser.add_argument('-cp', '--configpath', \
            help='adds a configration file to the config class', type=str)

        args = parser.parse_args()
        
        self.verbose = args.verbose
        
        if args.configpath:
            #OBS : overwrites class attributes 
            self.load_json_config(args.configpath)

    def load_json_config(self, path):
        """takes a 'json' file and sets its attributes to it self
            path : path (to a json file)
        """
        token = filehandler.json_decoder(path)

        for key, value in token.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{ self.__class__ } : { self.__dict__ }"

    def __repr__(self):
        return f"{ self.__class__ }  in module: { self.__module__ } at <{ hex(id(self)) }>"


####### GLOBAL CONFIG   ##########

DEFAULT_CONFIG = os.path.join('config', 'default.json')

conf = Config(DEFAULT_CONFIG)















