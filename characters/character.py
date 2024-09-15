import json
import os

class Character():
    def __init__(self, characterKey: str = "", art: str = "", description: str = "" ) -> None:
        if not characterKey:
            self.loadCharacterFromKey("unknown")
        else:
            self.loadCharacterFromKey(characterKey)

    def __str__(self):
        return f"Character: {{ name: {self.name}, art: {self.art}, description: {self.description} }}"
    
    def loadCharacterFromKey(self, characterKey):
        file_path = 'character\character.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data: dict[str, dict] = json.load(file)
                characterData: dict[str, dict] = data[characterKey]
            with open(characterData['art'], 'r') as f:
                self.art = f.read()
            self.name = characterKey.capitalize()
            self.description = characterData['description']
        else:
            self.createCharacter()

    def printArt(self) -> None:
        print(self.art)

    def printCharacterIntro(self) -> None:
        print(self.name)
        self.printArt()
        print(self.description)

    def createCharacter(self) -> None:
        # Ask player what their name is 
        # Accept user input from command line
        # When type name say hello "name"
        self.name = input("What is you name?\n")
        print(self.name)
        self.description = input("What is your tale?\n")
        self.art = ""
 