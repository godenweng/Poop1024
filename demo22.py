from typing import Literal


def setDirection(direction):
    if direction == "EAST":
        print("0")
    elif direction == "NORTH":
        print("90")
    elif direction == "WEST":
        print("180")
    elif direction == "SOUTH":
        print("270")
    else:
        print("not direction ==", direction)


setDirection("EAST")
setDirection("NORTH")
setDirection("WEST")
setDirection("APPLE")
setDirection("SOUTH")
print()


def setDirection2(direction: Literal["EAST", "NORTH", "WEST", "SOUTH"]) -> None:
    if direction == "EAST":
        print("0")
    elif direction == "NORTH":
        print("90")
    elif direction == "WEST":
        print("180")
    elif direction == "SOUTH":
        print("270")
    else:
        print("********")


setDirection2("EAST")
setDirection2("NORTH")
setDirection2("WEST")
setDirection2("APPLE")
setDirection2("SOUTH")
