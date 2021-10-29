class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def getDensity(self):
        return self.value / self.weight
    def __str__(self):
        return self.name + ' < ' + str(self.value) + ', ' + str(self.weight) + ' > '

def buildMenu(names, values, weights):
    menu = []
    for i in range(len(names)):
        menu.append(Item(names[i], values[i], weights[i]))
    return menu

def greedy(items, capacity, bestFunction):    
    sortedItems = sorted(items, key = bestFunction, reverse = True)
    result = []
    totalValue, remainWeight = 0.0, capacity

    for i in range(len(sortedItems)):
        if(sortedItems[i].getWeight() <= remainWeight):
            result.append(sortedItems[i])
            totalValue += sortedItems[i].getValue()
            remainWeight -= sortedItems[i].getWeight()
    return (result, totalValue)

def testGreedy(items, capacity, bestFunction):
    result, value = greedy(items, capacity, bestFunction)
    print('Value', value, end='\n')
    for item in result:
        print(item, end='\n')
    
def testGreedys(items, capacity):
    print('Value as best function', end='\n')
    testGreedy(items, capacity, Item.getValue)
    print('Weight as best function', end='\n')
    testGreedy(items, capacity, lambda item: 1/Item.getWeight(item))
    print('Density as best function', end='\n')
    testGreedy(items, capacity, Item.getDensity)

def convertToBinary(number, n):
    binary = [0]*n
    index = n-1
    while(number):
        binary[index] = number%2
        number //= 2
        index -= 1
    return binary

def isValidCombination(items, combination, capacity):
    currentCapacity = 0
    for item in range(len(combination)):
        if(combination[item]):
            currentCapacity += items[item].getWeight()
    return currentCapacity <= capacity

def bruteForce(items, capacity):
    n = len(items)
    size = 2**n
    allCombinations = []
    for i in range(size):
        allCombinations.append(convertToBinary(i, n))
    
    validCombinations = []
    for combination in allCombinations:
        if(isValidCombination(items, combination, capacity)):
            validCombinations.append(combination)

    bestCombination, bestValue = [], 0

    for combination in range(len(validCombinations)):
        currentValue = 0.0
        for item in range(len(validCombinations[combination])):
            if(validCombinations[combination][item]):
                currentValue += items[item].getValue()
        if(currentValue >= bestValue):
            bestValue = currentValue
            bestCombination = validCombinations[combination]
    
    result = []
    for item in range(len(bestCombination)):
        if(bestCombination[item]):
            result.append(items[item])

    return result, bestValue

def testBruteForce(items, capacity):
    result, value = bruteForce(items, capacity)
    print('Value', value, end='\n')
    for item in result:
        print(item, end='\n')


names = ['wine', 'beer', 'pizza', 'burger']
values = [89,90,95,100]
weights = [123,154,258,354]

items = buildMenu(names, values, weights)
capacity = 500
print('Brute Force', end='\n')
testBruteForce(items ,capacity)
print('Greedy', end='\n')
testGreedys(items ,capacity)