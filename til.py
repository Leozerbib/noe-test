import json
from datetime import date
import os

HOME = os.path.dirname(os.path.abspath(__file__))
DATALAKE_ROOT_FOLDER = HOME + "/datalake/"


def store(rf,source,entity,response):
    TARGET_PATH = getPath(rf,source,entity)

    storeDir(response,TARGET_PATH)

def getPath(rf,source,entity):
    TARGET_PATH = DATALAKE_ROOT_FOLDER
    if rf:
        TARGET_PATH = raw(source,entity,TARGET_PATH)
    else :
        TARGET_PATH = formated(source,entity,TARGET_PATH)
    return TARGET_PATH

def raw(source,entity,path):
    path += "raw/"
    return sources(source,entity,path)
   
def formated(source,entity,path):
    path += "formated/"
    return sources(source,entity,path)


def sources(source,entity,path):
    if source == 1:
        path += "Twitch/"
        return entitysource1(entity,path)
    if source == 2:
        path += "Jeu/"
        return entitysource2(entity,path)

def entitysource1(entity,path):
    if entity == 1:
        path += "game/top1000games/"
    if entity == 2:
        path += "game/topStreamTopGame/"
    return path

def entitysource2(entity,path):
    if entity == 1:
        path += "jeu/info/"
    if entity == 2:
        path += "enum/age_rating/"
    if entity == 3:
        path += "enum/game_engine/"
    if entity == 4:
        path += "enum/game_mode/"
    if entity == 5:
        path += "enum/game_genre/"
    if entity == 6:
        path += "enum/game_language/"
    if entity == 7:
        path += "enum/game_langue/"
    if entity == 8:
        path += "enum/game_theme/"
    if entity == 9:
        path += "enum/game_loca/"
    if entity == 10:
        path += "enum/game_platform/"
    return path

def storeDir(response,path):
    print("Writing here: ", path)
    current_day = date.today().strftime("%Y%m%d")
    if not os.path.exists(path):
       os.makedirs(path)
    print("Writing here: ", path)
    f = open(path + "response.json", "w+")
    f.write(json.dumps(response, indent=4))