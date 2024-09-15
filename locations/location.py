import json

class  Location():
    def __init__(self, locationKey: str = None) -> None:
        if locationKey:
            self.loadLocationData(locationKey)
        else:
            self.loadLocationData()

    def loadLocationData(self, locationKey: str = "prison") -> None:
        self.name = locationKey.capitalize()
        with open('locations/locations.json', 'r') as file:
            data = json.load(file)
            locationData: dict[str, dict] = data[locationKey]
            self.description = locationData['description']
        with open(locationData['art'], 'r') as l:
            self.art = l.read()
    
    def printArt(self) -> None:
        print(self.art)

    def printLocation(self) -> None:
        print(self.name)
        self.printArt()
        print(self.description)

    def __str__(self):
        return f"Location: {{ name: {self.name}, art: {self.art}, description: {self.description} }}"
    

