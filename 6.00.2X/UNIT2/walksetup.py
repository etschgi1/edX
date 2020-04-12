import random


class Location(object):
    """Models a location using x and y similar to a 2D graph"""

    def __init__(self, x, y):
        '''x and y are floats'''
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        '''deltaX and deltY are floats returns sum of coordinates + deltaval'''
        return Location(self.x+deltaX, self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        """gets distance from 'other' location obj to self returns a float"""
        ox = other.getX()
        oy = other.getY()
        xDist = self.getX()-ox
        yDist = self.getY()-oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x)+'|'+str(self.y)+'>'


class Field(object):
    """Models a field with drunks in it (using dict) drunks are keys 
    their location are corresponding values
    """

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        """Adds location of drunk(key) to the field(vals)"""
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        """Gets location of given drunk if in drunks"""
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        """moves a drunk if drunk in field to new location"""
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)


class Drunk(object):
    """Parent class for different kind of drunks 
    Drunk has a name
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):
    """
    Usual Drunks can step in 4 directions each step has same lenght
    """

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):
    """
    Cold Drunk has a bias for stepping further south on the 2D Plane
    """

    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
