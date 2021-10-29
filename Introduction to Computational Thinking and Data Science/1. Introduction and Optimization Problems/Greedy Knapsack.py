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


names = ['wine', 'beer', 'pizza', 'burger',
        'fries', 'cola', 'apple', 'donut']
values = [89,90,95,100,90,79,50,10]
weights = [123,154,258,354,365,150,95,195]

items = buildMenu(names, values, weights)
capacity = 1000
testGreedys(items ,capacity)
testBruteForce(items ,capacity)