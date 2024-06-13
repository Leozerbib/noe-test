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
        path += "PlateformStreaming/"
        return entitysource1(entity,path)
    if source == 2:
        path += "ListFilm/"
        return entitysource2(entity,path)

def entitysource1(entity,path):
    if entity == 1:
        path += "enum/plateform/"
    if entity == 2:
        path += "gares/"
    return path

def entitysource2(entity,path):
    if entity == 1:
        path += "enum/countries/"
    if entity == 2:
        path += "enum/languages/"
    if entity == 3:
        path += "enum/genres/"
    return path

def storeDir(response,path):
    print("Writing here: ", path)
    current_day = date.today().strftime("%Y%m%d")
    if not os.path.exists(path):
       os.makedirs(path)
    print("Writing here: ", path)
    f = open(path + "response.json", "w+")
    f.write(json.dumps(response, indent=4))