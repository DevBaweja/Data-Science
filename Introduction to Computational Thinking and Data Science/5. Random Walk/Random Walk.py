import matplotlib.pyplot as plt
import pylab
import random


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def changeLocation(self, deltaX, deltaY):
        return Location(self.x + deltaX,
                        self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDistance(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Drunk(object):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class UnusualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk Absent')

        deltaX, deltaY = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].changeLocation(deltaX, deltaY)

    def getLocation(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk Absent')
        return self.drunks[drunk]


def singleWalk(field, drunk, step):
    start = field.getLocation(drunk)

    for _ in range(step):
        field.moveDrunk(drunk)

    finish = field.getLocation(drunk)
    return (finish, start.getDistance(finish))


def simulateWalk(step, trials, drunkType):
    drunk = drunkType()
    origin = Location(0, 0)
    distances = []
    locations = []
    for _ in range(trials):
        field = Field()
        field.addDrunk(drunk, origin)
        location, distance = singleWalk(field, drunk, step)
        distances.append(round(distance, 1))
        locations.append(location)

    return (locations, distances)


def testDrunk(steps, trials, drunkType):
    means = []

    for step in steps:
        locations, distances = simulateWalk(step, trials, drunkType)
        print(drunkType.__name__, ' walk of ', step, ' steps.')
        mean = round(sum(distances)/len(distances), 2)
        means.append(mean)
        print(' Mean: ', mean)
        print(' Max: ', max(distances), ' Min: ', min(distances))

    return means, locations


random.seed(0)


def simulateDrunk(drunkTypes, steps, trials):
    plotsteps, plotmeans, plotVals, plotDrunkTypes = [], [], [], []
    for drunkType in drunkTypes:
        means, locations = testDrunk(steps, trials, drunkType)
        xVals, yVals = [], []
        for location in locations:
            xVals.append(location.getX())
            yVals.append(location.getY())

        plotsteps.append(steps)
        plotmeans.append(means)
        plotDrunkTypes.append(drunkType.__name__)

        plotVals.append((xVals, yVals))

    return (plotsteps, plotmeans, plotVals, plotDrunkTypes)


def displayPlots(plotsteps, plotmeans, plotVals, plotDrunkTypes):
    for index in range(len(plotsteps)):
        steps = plotsteps[index]
        means = plotmeans[index]
        drunkType = plotDrunkTypes[index]
        pylab.plot(steps, means, label=drunkType)
        pylab.title('Mean Distance')
        pylab.xlabel('Steps')
        pylab.ylabel('Distance')
        pylab.legend(loc='best')
    plt.show()

    styles = ['bo', 'k+']
    for index in range(len(plotVals)):
        xVals, yVals = plotVals[index]
        drunkType = plotDrunkTypes[index]
        style = styles[index]
        meanX = round(sum(xVals)/len(xVals), 2)
        meanY = round(sum(yVals)/len(yVals), 2)
        pylab.plot(xVals, yVals, style, label=drunkType +
                   ' Mean Distance <' + str(meanX) + ', ' + str(meanY) + '>')
        pylab.title('Locations')
        pylab.ylim(-1000, 1000)
        pylab.xlim(-1000, 1000)
        pylab.xlabel('East - West')
        pylab.ylabel('North - South')
        pylab.legend(loc='lower center')
    plt.show()


steps = (10, 100, 1000, 10000)
trials = 100
drunkTypes = (UsualDrunk, UnusualDrunk)

plotsteps, plotmeans, plotVals, plotDrunkTypes = simulateDrunk(
    drunkTypes, steps, trials)
displayPlots(plotsteps, plotmeans, plotVals, plotDrunkTypes)


class OddField(Field):
    def __init__(self, holes=1000, xRange=100, yRange=100):
        Field.__init__(self)
        self.wormholes = {}
        for _ in range(holes):
            oldx = random.randint(-xRange, xRange)
            oldy = random.randint(-yRange, yRange)
            newx = random.randint(-yRange, yRange)
            newy = random.randint(-yRange, yRange)
            self.wormholes[(oldx, oldy)] = Location(newx, newy)

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()

        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


def traceWalk(fieldTypes, steps):
    styles = ['bo', 'k+']
    for index in range(len(fieldTypes)):
        fieldType = fieldTypes[index]
        style = styles[index]
        drunk = UsualDrunk()
        field = fieldType()
        field.addDrunk(drunk, Location(0, 0))
        locations = []

        for _ in range(steps):
            field.moveDrunk(drunk)
            location = field.getLocation(drunk)
            locations.append(location)

        xVals, yVals = [], []
        for location in locations:
            xVals.append(location.getX())
            yVals.append(location.getY())

        pylab.plot(xVals, yVals, style)
        pylab.title('Location Visited')
        pylab.xlabel('East-West of Origin')
        pylab.ylabel('North-South of Origin')

    plt.show()


fieldTypes = (Field, OddField)
traceWalk(fieldTypes, 1000)
