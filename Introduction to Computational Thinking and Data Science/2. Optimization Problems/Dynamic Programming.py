import random


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


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fibDP(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibDP(n-1)+fibDP(n-2)
    return memo[n]


for el in range(100):
    # print('fib(', el, '): ', fib(el), end='\n')
    print('fib(', el, '): ', fibDP(el), end='\n')


def searchTree(toConsider, available):
    if toConsider == [] or available == 0:
        return (0, ())
    else:
        nextItem, *remainItem = toConsider
        withoutValue, withoutToTake = searchTree(toConsider[1:], available)
        # Optimization of unneeded branches
        if nextItem.getWeight() <= available:
            withValue, withToTake = searchTree(
                toConsider[1:], available - nextItem.getWeight())
            withValue += nextItem.getValue()
            if withValue > withoutValue:
                return (withValue, withToTake + (nextItem,))
    return (withoutValue, withoutToTake)


def searchTreeDP(toConsider, available, memo={}):
    if toConsider == [] or available == 0:
        return (0, ())
    elif (len(toConsider), available) in memo:
        return memo[(len(toConsider), available)]
    else:
        nextItem, *remainItem = toConsider
        withoutValue, withoutToTake = searchTreeDP(
            toConsider[1:], available, memo)
        # Optimization of unneeded branches
        if nextItem.getWeight() <= available:
            withValue, withToTake = searchTreeDP(
                toConsider[1:], available - nextItem.getWeight(), memo)
            withValue += nextItem.getValue()
            if withValue > withoutValue:
                memo[(len(toConsider), available)] = (
                    withValue, withToTake + (nextItem,))
                return memo[(len(toConsider), available)]
    memo[(len(toConsider), available)] = (withoutValue, withoutToTake)
    return memo[(len(toConsider), available)]


def testSearchTree(items, capacity, algorithm):
    value, result = algorithm(items, capacity)
    print('Value', value, end='\n')
    for item in result:
        print(item, end='\n')


names = ['wine', 'beer', 'pizza', 'burger',
         'fries', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
weights = [123, 154, 258, 354, 365, 150, 95, 195]

items = buildMenu(names, values, weights)
capacity = 750
print('Search Tree', end='\n')
# testSearchTree(items, capacity, searchTree)
print('Dynamic Programming', end='\n')
testSearchTree(items, capacity, searchTreeDP)


def buildLargeMenu(numItems, maxValue, maxWeight):
    items = []
    for el in range(numItems):
        item = Item(str(el), random.randint(1, maxValue),
                    random.randint(1, maxWeight))
        items.append(item)
    return items


maxValue = 100
maxWeight = 250

for numItems in range(5, 50, 5):
    items = buildLargeMenu(numItems, maxValue, maxWeight)
    # testSearchTree(items, capacity, searchTree)
    testSearchTree(items, capacity, searchTreeDP)
