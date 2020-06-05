# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

import numpy as np

##################
# Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
# from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5

# For Python 3.6:
# from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6

# Exceptions: Custom


class WidthHeightError(Exception):
    pass


# === Provided class Position
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


# Problem 1 done


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


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        # spawn location of robot
        self.position = room.getRandomPosition()
        # clean spawn
        self.room.cleanTileAtPosition(self.position)
        # sets up random direction 0<=direction<360
        self.direction = random.random()*360

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        no return!
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        no return!
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        raise NotImplementedError  # don't change this!


# === Problem 3


class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # set temp position to check if temp is valid position
        temp = self.position.getNewPosition(self.direction,
                                            self.speed)
        # if valid proceed and clean tile
        if self.room.isPositionInRoom(temp) == True:
            self.position = temp
        # else loop as long using different directions till you get valid pos
        else:
            while True:
                self.direction = random.random()*360
                temp = self.position.getNewPosition(self.direction, self.speed)
                # same check as above
                if self.room.isPositionInRoom(temp) == True:
                    self.position = temp
                    break
        # clean tile at valid position
        self.room.cleanTileAtPosition(self.position)


class Smartrobot(Robot):
    """
    Hint not so smart yet
    A Smartrobot is a Robot with the smart movement strategy.

    At each time-step, a Smartrobot attempts to move in its current
    direction; when it would hit a wall or a cleaned block, it *instead*
    chooses a new direction either 90° turn right or left
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # for first move change direction to a multiple of 90°
        if self.room.getNumCleanedTiles() == 1:
            self.setRobotDirection(random.choice([0, 90, 180, 270]))
        # move until wall collision
        temp = self.position.getNewPosition(self.direction, self.speed)
        # get position
        pos = temp
        x = int(pos.getX())
        y = int(pos.getY())
        # Check if Temp is valid
        if self.room.isPositionInRoom(temp) == True:
            # if temp not cleaned move on
            if self.room.isTileCleaned(x, y) == False:
                self.position = temp
                self.room.cleanTileAtPosition(self.position)
                return None
            # if cleaned
            else:
                self.direction = random.choice([0, 90, 180, 270])
                self.position = temp
                self.room.cleanTileAtPosition(self.position)
                return None

        # if on border
        elif self.room.isPositionInRoom(temp) == False:
            while True:
                if self.direction < 270:
                    self.direction += 90
                else:
                    self.direction = 0
                temp = self.position.getNewPosition(self.direction, self.speed)
                if self.room.isPositionInRoom(temp) == True:
                    self.position = temp
                    break

        # if theres no clean tile choose a multiple of 90° at random

        # clean tile
        self.room.cleanTileAtPosition(self.position)

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    times = []
    while 0 < num_trials:
        timestep = 0
        # anim = ps2_visualize.RobotVisualization(
        # num_robots, width, height, 0.08)
        # loop for each simultation run num_trials times:
        room = RectangularRoom(width, height)
        # initialise robots in list:
        robots = []
        for i in range(num_robots):
            robots.append(robot_type(room, speed))
        # run as long as min_coverage > calcCoverage()
        while min_coverage > calcCoverage(room):
            # main robot simulation each loop one move
            # every robot updates pos and cleans tile:
            for robot in robots:
                robot.updatePositionAndClean()
                #anim.update(room, robots)
            # timestep +1
            timestep += 1
        # add time of simulation to simulations times
        # anim.done()
        times.append(timestep)
        # num_trial -1
        num_trials -= 1

    # calculate mean number of time steps
    return (sum(times)/len(times))


def calcCoverage(room):
    """[input room. returns a val between 0 and 1 which translates to
    percentage of room cleaned]
    Arguments:
        room {[room-type]} -- [Room which is cleaned by robots]
    """
    return room.getNumCleanedTiles()/room.getNumTiles()


# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(1, 1.0, 10, 10, 1, 1, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # added one line to make it random for normal step
        self.direction = random.random()*360
        # set temp position to check if temp is valid position
        temp = self.position.getNewPosition(self.direction,
                                            self.speed)
        # if valid proceed and clean tile
        if self.room.isPositionInRoom(temp) == True:
            self.position = temp
        # else loop as long using different directions till you get valid pos
        else:
            while True:
                self.direction = random.random()*360
                temp = self.position.getNewPosition(self.direction, self.speed)
                # same check as above
                if self.room.isPositionInRoom(temp) == True:
                    self.position = temp
                    break
        # clean tile at valid position
        self.room.cleanTileAtPosition(self.position)


#print(runSimulation(1, 1.0, 10, 10, 1, 1, RandomWalkRobot))


def showPlot1(title, x_label, y_label):
    """
    Plots num of robots against time for standard and random walk
    robot subclass
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    times3 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0,
                                    20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0,
                                    20, 20, 0.8, 20, RandomWalkRobot))
        times3.append(runSimulation(num_robots, 1.0,
                                    20, 20, 0.8, 20, Smartrobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.plot(num_robot_range, times3)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot',
                  'SmartRobot(not so smart)'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    times3 = []
    for width in [10, 17.32, 20, 25, 30]:
        height = 300//width
        print("Plotting cleaning time for a room of width:",
              width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(
            2, 1.0, width, height, 0.8, 20, StandardRobot))
        times2.append(runSimulation(
            2, 1.0, width, height, 0.8, 20, RandomWalkRobot))
        times3.append(runSimulation(
            2, 1.0, width, height, 0.8, 20, Smartrobot))
    print(aspect_ratios)
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.plot(aspect_ratios, times3)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot',
                  'SmartRobot(not so smart)'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# === Problem 6
# NOTE: If you are running the simulation, you will have to close it
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#
showPlot1("Time It Takes 1 - 10 Robots To Clean 80% Of A 20x20 Room",
          "Robots", "Cleaning Time in Ticks")
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
showPlot2("Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms",
          "Aspect Ratio", "Cleaning Time in Ticks")
#
