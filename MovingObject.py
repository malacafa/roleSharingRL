from MakeMission import MakeMission

class Car:
    def __init__(self, name):
        self.pos = self.setPos(name)
        self.name = name
        self.bag = 0

        self.makeMission = MakeMission()

    def setPos(self, name):
        if name == 'A':
            return []

        if name == 'B':
            return []

        if name == 'C':
            return []

    def move(self, action):
        if action == 0:
            self.pos[1] -= 1
        if action == 1:
            self.pos[0] += 1
        if action == 2:
            self.pos[1] += 1
        if action == 3:
            self.pos[0] -= 1
        
        

class Human:
    def __init__(self):
        self.pos = []
        