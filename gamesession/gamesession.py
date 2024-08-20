import json

from datetime import datetime
from characters.character import Character
from locations.location import Location

class GameSession():
    def __init__(self, path: str = "", location: str = "") -> None:
        if not path:
            # create a new game session
            # TODO: set location
            self.location = Location(location)
            print("location created")
            # TODO: set character
            self.character = Character()
            print("character created")
            # TODO: Create a game save file in /saves with filename "DATETIME-character-name.json"
            # self.saveGame()
        else:
            print("not yet implemented")
            # self.character = Character()

    def saveGame(self): 
        now =  datetime.now()
        name = self.character.name
        filename = "/saves/" + now.strftime('%Y-%m-%d-%H-%M') + "-" + name # /saves/2024-01-13-stupidface.json
        print(filename)
        # with open(filename) as f:
        #     data = self.__dict__
        #     json.dump(data, f)
