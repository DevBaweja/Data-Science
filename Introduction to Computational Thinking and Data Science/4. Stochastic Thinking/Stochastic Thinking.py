import random
import math

def rollDice():
    return random.choice([1,2,3,4,5,6])

def testRollDice(size):
    result = ''
    for _ in range(size):
        result += str(rollDice())
    return result

random.seed(0)

def runSim(size, goal, trials):
    total = 0
    for el in range(trials):
        result = testRollDice(size)
        if result == goal:
            total += 1
    print('Actual Probability: ', round(1/(6**size), 8))
    print('Estimated Probability: ', round(total/trials,8))

runSim(5, '11111', 1000000)

import matplotlib.pyplot as plot 

random.seed(0)
def sameDay(numPeople, degree, days):
    possibleDays = range(days)
    birthdays = [0]*days

    for _ in range(numPeople):
        birthdays[random.choice(possibleDays)] += 1

    return max(birthdays) >= degree

def birthdayProbability(numPeople, degree, numTrials, days):
    nums = 0
    for _ in range(numTrials):
        if(sameDay(numPeople, degree, days)):
            nums += 1
    return nums / numTrials

def birthdayParadox():
    # numPeoples = [10, 20, 40, 100]
    numPeoples = range(0, 100, 2)
    days = 365
    numTrials = 10000
    degree = 2
    actualPlot = []
    expectedPlot = []
    for numPeople in numPeoples:
        print('For: ', numPeople)
        numerator = math.factorial(days)
        denominator = (days**numPeople)*math.factorial(days-numPeople)
        actual = round(1 - numerator / denominator, 4)
        expected = birthdayProbability(numPeople, degree, numTrials, days)
        print('Actual: ', actual)
        print('Estimated: ', expected)
        actualPlot.append(actual)
        expectedPlot.append(expected)
  
    plt.plot(numPeoples, actualPlot)
    plt.show()
    plt.plot(numPeoples, expectedPlot)
    plt.show()
    size = len(numPeoples)
    difference  = []
    for index in range(size):
        difference.append(actualPlot[index]-expectedPlot[index])
    plt.plot(numPeoples,difference)
    plt.show()

birthdayParadox()