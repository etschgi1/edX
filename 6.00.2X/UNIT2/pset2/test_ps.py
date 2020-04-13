from ps2 import *


def create_test_room(width, height):
    '''creates a testroom with height/width'''
    return RectangularRoom(width, height)


def create_test_pos(num, room):
    '''creates num random pos inside room returns list'''
    out = []
    for i in range(num):
        out.append(RectangularRoom.getRandomPosition(room))
    return out


testroom = create_test_room(5, 10)
pos = create_test_pos(5, testroom)
print(testroom, pos)
testroom.cleanTileAtPosition(pos[0])
print(testroom.show_array())
