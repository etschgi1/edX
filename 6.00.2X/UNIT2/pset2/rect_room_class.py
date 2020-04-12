# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import random


class WidthHeightError(Exception):
    pass


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = int(width)
        self.height = int(height)
        if self.width <= 0 or self.height <= 0:
            raise WidthHeightError("Width or height cannot be 0 or smaller.")

        # get total tiles
        totaltiles = self.width * self.height
        # create numpyarray with 0 for dirty 1 for cleaned
        self.roomarray = np.zeros((self.height, self.width), dtype=int)

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # get positions from pos object
        # int to avoid indexing error cause pos can be float
        xwidthpos = int(pos.getX())
        yheightpos = int(pos.getY())
        # set location in roomarray to 1 for cleaned
        self.roomarray[yheightpos, xwidthpos] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.
        (0,0) represents top left tile
        m: an integer >=0
        n: an integer >=0
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.roomarray[n, m] == 1:
            return True
        return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # returns count of unique 1s in array [1][1] because unique() returns
        # 2 list first containing unique entries and secound their count
        # in ascending order
        unique, counts = np.unique(self.roomarray, return_counts=True)
        # both means list with 2 entries secound is counts
        if 1 in unique and 0 in unique:
            return counts[1]
        elif 0 in unique:
            return 0
        return counts[0]

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object. (float)
        """
        # width for max X Var and height for max Y (Origin top-left corner)
        return Position(random.random()*self.width,
                        random.random()*self.height)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        xwidthpos = pos.getX()
        yheightpos = pos.getY()
        # Checks if x and y pos are =>0 and not bigger than width and height
        if xwidthpos < self.width and xwidthpos >= 0 and \
                yheightpos < self.height and yheightpos >= 0:
            return True
        return False

    def show_array(self):
        '''Prints numpy array of room'''
        return self.roomarray


testroom = RectangularRoom(1, 3)
print(testroom.show_array())
print("num clean")
print(testroom.getNumCleanedTiles())

pos = Position(0, 0)
testroom.cleanTileAtPosition(pos)
pos = Position(0, 1)
testroom.cleanTileAtPosition(pos)
pos = Position(0, 2)
testroom.cleanTileAtPosition(pos)
print("num clean")
print(testroom.getNumCleanedTiles())
# print("numtiles")
# print(testroom.getNumTiles())
# print("-----------")

# testpos = Position(9, 2)
# testroom.cleanTileAtPosition(testpos)
# testpos = Position(9, 2)
# testroom.cleanTileAtPosition(testpos)
# print(testroom.show_array())
# print(testroom.isTileCleaned(8, 2))
# print(testroom.getNumCleanedTiles())
# testpos = Position(10, 3)
# print(testroom.isPositionInRoom(testpos))
# print(testpos.getX(), testpos.getY())
# print(testpos)
