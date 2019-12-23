import requests
import json
import configparser
import os
import constant
import boi

class Sweeps:
    # TODO: make auto config generation smoother. current issue: if config.ini does not have an api key/does not exist, init does not create one in time for other things to use it. May need some callbacks
    def __init__(self):
        config = configparser.ConfigParser()
        if os.path.isfile('config.ini'):
            configfile = config.read('config.ini')
            config.read('config.ini')
            self.key = config['User']['APIkey']
            self.bois = config['User']['bois']
        else:
            print("Config.ini not found. Creating with default values and fresh API key\n")
            APIKey = requests.get(constant.BASE_URL + "getNewAPIKey").json()
            print(APIKey)
            config.read('config.ini')
            config['User'] = {'APIKey': APIKey,
                              'bois': []}

            with open('config.ini', 'w') as configfile:
                config.write(configfile)

    def getmybois(self):
        body = json.dumps({'key': self.APIKey})
        return bois

    @staticmethod
    def getworldmap():
        m = requests.get(constant.BASE_URL + "getMap").json()
        return m

    @staticmethod
    def getsector(x, y):
        body = json.dumps({"x": 1, "y": 1})
        head = {"content-type": "application/json"}
        sector = requests.put(constant.BASE_URL + "getSector", data=body, headers=head).json()
        return sector
                              

    def getentity(self, id):
        ar = []
        for i in self.boiz:
            ar += requests.put(constant.BASE_URL+"entities/"+id, data=json.dumps({"APIKey": self.key}))

        return ar

    # TODO: get this working. currently gives a 415 error code for unknown reason.
    def createboi(self, x, y, sectorX, sectorY):
        body = json.dumps({"x": x, "y": y, "sectorX": sectorX, "sectorY": sectorY, "key": self.key})
        head = {"content-type": "application/json"}
        err = requests.put(constant.BASE_URL + "createInitialBoi", data = body, headers = head)
        return err

                               
