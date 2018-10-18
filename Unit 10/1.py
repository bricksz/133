'''

Add a new ‘Probing’ player type to Program 10.0.2 and rerun it starting with an
initial population of five players of each type: friendly, mean, mirror and probing.

A probing player attempts to identify the type of the other players. If playing against a
mean player or a nice one, it’s always nasty, protecting itself in the first case and
exploiting the vulnerable in the second.

If playing against a mirror player or another
probing player, it’s always nice, since the cooperative result is the best one possible.

To determine the type of the other player, the prober is always nasty in its first encounter
and nice in the second. The corresponding actions of the other player are always enough to
positively identify it.

If the other player is nice twice in a row, it must be a friendly player.

If it is nasty twice, it must be a mean player. If it is nice and then nasty,
it must be a mirror player.

And if it is nasty and then nice, it must be another prober.

'''

import random
class Player:
    idCounter = 0
    def __init__(self):
        self.score = 0
        self.memory = {}
        Player.idCounter += 1
        self.name = 'Player {0}'.format(Player.idCounter)
    def processResult(self, otherName,myResponse,otherResponse):
        result = [myResponse, otherResponse]
        if otherName in self.memory:
            self.memory[otherName].append(result)
        else:
            self.memory[otherName] = [result]
        if myResponse == 'nice' and otherResponse == 'nice':
            self.score += 30
        elif myResponse == 'nice' and otherResponse == 'nasty':
            self.score -= 70
        elif myResponse == 'nasty' and otherResponse == 'nice':
            self.score += 50
        else:
            self.score += 0

class FriendlyPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (friendly)'
    def respondsTo(self, otherName):
        return 'nice'

class MeanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mean)'
    def respondsTo(self, otherName):
        return 'nasty'

class MirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nice'

class ProbingPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (probing)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            record = self.memory[otherName]
            if len(record) == 1:
                return 'nice'
            elif record[0][1] == 'nice' and record[1][1] == 'nice':
                return 'nasty'
            if record[0][1] == 'nasty' and record[1][1] == 'nice':
                return 'nasty'
            else:
                return 'nice'
        else:
            return 'nasty'

def encounter(player1, player2):
    name1, name2 = player1.name, player2.name
    response1 = player1.respondsTo(name2)
    response2 = player2.respondsTo(name1)
    player1.processResult(name2, response1, response2)
    player2.processResult(name1, response2, response1)

def makePopulation(specs):
    population = []
    for playerType, number in specs:
        for player in range(number):
            population.append(playerType())
    return population

def doGeneration(population, numberOfEncounters):
    for encounterNumber in range(numberOfEncounters):
        players = random.sample(population, 2)
        encounter(players[0], players[1])

def sortPopulation(population):
    scoreList = [[player.score, player.name, type(player)]
                 for player in population]
    scoreList.sort()
    return scoreList

def report(scoreList):
    pattern = '{0:23s}{1:6d}'
    for score, name, playerType in scoreList:
        print(pattern.format(name, score))

def makeNextGeneration(scoreList):
    nextGeneration = []
    populationSize = len(scoreList)
    scoreList = scoreList[int(populationSize/2):]
    for score, name, playerType in scoreList:
        for number in range(2):
            nextGeneration.append(playerType())
    return nextGeneration



allPlayers = makePopulation([[FriendlyPlayer, 5],
                             [MeanPlayer, 5],
                             [MirrorPlayer, 5],
                             [ProbingPlayer, 5]
                             ])

pattern = '*** Generation: {0} ***\n'
for generationNumber in range(5):
    doGeneration(allPlayers, 2000)
    sortedResults = sortPopulation(allPlayers)
    print(pattern.format(generationNumber+1))
    report(sortedResults)
    allPlayers = makeNextGeneration(sortedResults)
    print()
