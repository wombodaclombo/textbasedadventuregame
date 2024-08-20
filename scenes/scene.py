class Scene:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

s = Scene("The cell block you are in is mark with letters that are no longer visible. As you look around you see a mound in the back corner and a couple of reptilian guards hanging around a steaming pot of somthing pungent")
print(s.__dict__)
