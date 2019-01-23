from Map import MapInfo
from random import randrange

class MakeMission:
    def __init__(self):
        self.mapInfo = MapInfo()
        self.mapList = self.mapInfo.getMap()
        self.missionPos = [None]*3
        self.doneList = [False, False, False]

    def reset(self):
        for i in range(3):
            pos = [randrange(27), randrange(25)]
            while pos not in self.missionPos and self.mapList[pos[0]][pos[1]] != 0:
                pos = [randrange(27), randrange(25)]

            self.missionPos[i] = pos
            self.doneList[i] = False
    
    def makeMission(self):
        for i in range(3):
            if self.doneList[i] == True:
                x, y = self.missionPos[i]
                self.mapList[x][y] = 0
                pos = [randrange(27), randrange(25)]
                while pos not in self.missionPos and self.mapList[pos[0]][pos[1]] != 0:
                    pos = [randrange(27), randrange(25)]

                self.missionPos[i] = pos
                self.doneList[i] = False

        no = 1
        for x,y in self.missionPos:
            self.mapList[x][y] = 'M'+str(no)
            no+=1

    def getMissionPos(self):
        return self.missionPos
    
    def getMissionAddedMap(self):
        return self.mapList

if __name__ == '__main__':
    makeMission = makeMission()
    makeMission.reset()
    missionList = makeMission.getMissionPos()
    mapList = makeMission.getMissionAddedMap()
    print(missionList)
    print(mapList)