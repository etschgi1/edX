class Food(object):
    '''
    Class to model Foods 
    takes name, value and calories of food
    custom print mod
    '''

    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ": ("+str(self.getValue())+", "\
            + str(self.getCost())+")"


def buildMenu(names, values, calories):
    '''builds menus of 3 list with same lenght
    returns list filled with foods
    '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    '''Assumes items a list, maxCost >= 0, 
    keyFunc maps elements of items to numbers
    returns 2 lists: result (with taken foods in this list)
    and totelVal - Value of all foods combined'''
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totelVal, totalCal = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCal+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCal += itemsCopy[i].getCost()
            totelVal += itemsCopy[i].getValue()
    return result, totelVal


def testGreedy(items, constraint, keyFunction):
    '''
    test Function on Greedy; takes items (e.g. return of menu) 
    constraint = max. of Calories you'd like to eat
    keyFunction = function for sorting and evaluation "items", 
    e.g. sort by density of food, or calories 
    '''
    resulttaken, totelVal = greedy(items, constraint, keyFunction)
    print('Total Value of Items: ', totelVal)
    for singleresult in resulttaken:
        print("   ", singleresult)


def testGreedys(itmes, maxUnits):
    '''
    Helper function calls test Greedy 3 times using either: Value, Calories or
    density for sort each time
    '''
    print('\nGreedy by value')
    testGreedy(itmes, maxUnits, Food.getValue)
    print('\nGreedy by calories')
    testGreedy(itmes, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nGreedy by density')
    testGreedy(itmes, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger',
         'fries', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
# builds menu with specified lists above
menufoods = buildMenu(names, values, calories)
testGreedys(menufoods, 500)  # finds out best food for menu with cal limit
