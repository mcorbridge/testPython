

class PlayWithDict:

    def __init__(self):
        print("playing with dictionaries")
        self.dict0 = {}
        self.dict1 = {}

    def makeDict(self):
        self.dict0  = {
            "Boston":"Bruins",
            "Toronto": "Maple Leafs",
            "Montreal": "Canadiens",
            "New York": "Rangers",
            "Detroit": "Red Wings",
            "Chicago": "Black Hawks",
            "St Louis": "Blues",
            "Tampa": "Lightning",
            "Florida": "Panthers",
            "Philadelphia": "Flyers"
        }

        player0 = HockeyPlayer()
        player0.name = "Austin Matthews"
        player0.position = "center"

        player1 = HockeyPlayer()
        player1.name = "Mitch Marner"
        player1.position = "left wing"

        player2 = HockeyPlayer()
        player2.name = "John Tavares"
        player2.position = "center"

        bostonPlayers = [{"name":"Patrice Bergeron","position":"center"},
                         {"name":"Brad Marchand","position":"left wing"},
                         {"name":"Tory Krug","position":"left defense"}]
        torontoPlayers = (player0, player1, player2)
        montrealPlayers = ("Max Domi", "Brendan Gallagher", "Jesperi Kotkaniemi")
        newYorkPlayers = ("Jesper Fast", "Chris Kreider", "Boo Nieves")

        self.dict1 = dict(Boston=bostonPlayers, Toronto=torontoPlayers, Montreal=montrealPlayers, NewYork=newYorkPlayers)

    def printDict(self):
        print(self.dict0)
        print(self.dict1)
        print(self.dict1["Boston"])
        print(self.dict1["Boston"][0]["name"])
        self.dict1["Boston"][0] = "Zdeno Chara"
        print(self.dict1["Boston"])
        print(self.dict1["Toronto"][0])
        torontoPlayer = self.dict1["Toronto"][0]
        print(torontoPlayer.name)
        print()
        for f in dir(torontoPlayer):
            if f.find('_'):
                print(eval('f'))
        print(eval('f'))
        print(torontoPlayer.position)
        print(getattr(torontoPlayer, "position"))

        print(self.dict1.get('Toronto')[0].name)

class HockeyPlayer:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

playWithDict = PlayWithDict()

playWithDict.makeDict()

playWithDict.printDict()