import json
import os

class Character():
    def __init__(self, characterKey: str = "unknown") -> None:
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
            self.name = characterKey
            self.description = ""
            self.art = ""
        print(self)
    
    def printArt(self) -> None:
        print(self.art)

    def printCharacterIntro(self) -> None:
        print(self.name)
        self.printArt()
        print(self.description)

    def __str__(self):
        return f"Character: {{ name: {self.name}, art: {self.art}, description: {self.description} }}"