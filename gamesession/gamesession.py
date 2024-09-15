import json

from datetime import datetime
import os
from characters.character import Character
from locations.location import Location
from config import ROOT_DIR

class GameSession():
    def __init__(self, path: str = "") -> None:
        if not path:
            # create a new game session
            self.location = Location()
            self.character = Character()    
            self.saveGame()
        else:
            # if there is a path then
            self.loadGame(ROOT_DIR+ "/saves/"+ path)

    # TODO: Add minutes to save game file names to avoid duplicate file names
    def saveGame(self): 
        now =  datetime.now()
        name = self.character.name
        filename = now.strftime('%Y-%m-%d-%H-%M') + "-" + name + ".json" # /saves/2024-01-13-stupidface.json
        print(filename)
        session_data = self.to_dict()
        file_path = os.path.join(ROOT_DIR, "saves", filename)
        with open(file_path , "x") as f:
            json.dump(session_data, f)

    def loadGame(self, path: str):
        print("path", path)
        # load save game json file
        with open(path, "r") as f:
            data = json.loads(f)
        # extract the character data into this file
        self.character = Character(characterKey=data.character.name, art=data.character.art, description=data.character.description)
        # extract location data
        self.location = Location(data.location.name)

    def to_dict(self):
        dict = self.__dict__
        dict["character"] = self.character.__dict__
        dict["location"] = self.location.__dict__
        return dict