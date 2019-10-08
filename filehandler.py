#!bin/bash/python3
#######################################################
#   file handler - deals with reading, writing, loading 
#                    and  file stuff
#
#   author  : the kid 
#   version : 0.0.1
#   date    : oct 2019
#
########################################################

import os
import json

import pygame 

##############      JSON FILES      ##############################

def json_decoder(path):
    """deserializes python object from a '.json' file
        returns object. returns None in case of failure  
        str : path (must be a json file )
    """

    if not path.split('.')[-1] == 'json':
        raise Exception(f"[!] File format error: file {path} \
            must be a json file")
        
    token = None
    try:
        with open(path, 'r') as data:
            token = json.loads(data.read())

    except FileNotFoundError as e:
        e(f"[!] File not found error: file {path} doesn't exist")
    except PermissionError as e:
        e(f"[!] File permmited error: file {path} access not allowed")
    finally:
        return token

def json_encoder(obj, path):
    """serializes a python object in path
        returns True in case of success
        False in case of failure 
        *** overwrites file ***
        obj  : python object 
        path : str
    """
    if not path.split('.')[-1] == 'json':
        raise Exception(f"[!] File format error: file {path} \
            must be a json file")
    
    token = False 
    try:
        with open(path, 'w') as data:
            data.write(json.dumps(obj, indent=4, sort_keys=True))
            token = True

    except PermissionError as e:
        e(f"[!] File permmited error: file {path} access not allowed")
    finally:
        return token 
        

