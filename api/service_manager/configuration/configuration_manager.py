import os
import json

class ConfigurationManager(dict):
    def __init__(self, environment):
        filename = "configuration/{}.json".format(environment)
        if not os.path.isfile(filename):
            raise Exception("Not found")
        
        with open(filename, "r") as file:
            super().__init__(json.load(file))
