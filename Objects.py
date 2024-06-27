class Player:
    def __init__(self, player_id = "", bat_order = "", first_name = "", last_name = "", position = "", at_bats = 0, hits = 0):
        self.__player_id = player_id
        self.__bat_order = bat_order
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__at_bats = at_bats
        self.__hits = hits

    def getPlayerID(self):
        return self.__player_id
    
    def setPlayerID(self, player_id):
        self.__player_id = player_id

    def getBatOrder(self):
        return self.__bat_order
    
    def setBatOrder(self, bat_order):
        self.__bat_order = bat_order
    
    def getFirstName(self):
        return self.__first_name
    
    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getLastName(self):
        return self.__last_name
    
    def setLastName(self, last_name):
        self.__last_name = last_name

    def getPosition(self):
        return self.__position
    
    def setPosition(self, position):
        self.__position = position

    def getAtBats(self):
        return self.__at_bats
    
    def setAtBats(self, at_bats):
        self.__at_bats = at_bats

    def getHits(self):
        return self.__hits
    
    def setHits(self, hits):
        self.__hits = hits

    def getFullName(self):
        return self.__first_name + " " + self.__last_name
    
    def getBattingAverage(self):
        return int(self.__at_bats) / int(self.__hits)

class Lineup:
    def __init__(self):
        self.__lineup = []

    def addPlayer(self, player):
        self.__lineup.append(player)

    def removePlayer(self, player):
        self.__lineup_number -= self.__lineup[player]
        return self.__lineup.pop(player)

    def getPlayer(self, lineup_number):
        for player in self:
            if player.__lineup_number == lineup_number:
                return player
    
    def getLineupNumber(self): 
        return self.__index + 1

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineup) - 1:
            raise StopIteration
        
        self.__index += 1
        card = self.__lineup[self.__index]
        return card