import json

class Location():
    def __init__(self, locationKey: str) -> None:
        with open('locations/locations.json', 'r') as file:
            data = json.load(file)
            locationData: dict[str, dict] = data[locationKey]
        with open(locationData['art'], 'r') as l:
            self.art = l.read()
        self.name = locationKey.capitalize()
        self.description = locationData['description']
    
    def printArt(self) -> None:
        print(self.art)

    def printLocation(self) -> None:
        print(self.name)
        self.printArt()
        print(self.description)

    def __str__(self):
        return f"Location: {{ name: {self.name}, art: {self.art}, description: {self.description} }}"
    

