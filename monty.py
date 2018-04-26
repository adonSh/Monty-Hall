#!/usr/bin/env python3
import random
import argparse

###### DEFINITIONS ############

class Door:
    def __init__(self, win):
        self._win = win
    def isitawin(self):
        return self._win

# selects a door at random, removes a losing door, and
# returns a tuple containing the choice and the remaining door
def pickadoor(doors):
    guess = random.randint(0, 2)
    door = doors[guess]
    doors.remove(door)

    for d in doors:
        if not d.isitawin():
            doors.remove(d)

    return (door, doors[0])

# doors is a tuple (initial choice, other door), switch is a boolean
# returns true if the chosen door is a winner
def switch(doors, switch):
    if switch:
        return doors[1].isitawin()
    else:
        return doors[0].isitawin()

def parse_args(p):
    parser.add_argument('-s', '--switch', dest='switch', action='store_const',
                        const=True,
                        help='switch after the first door is revealed')
    parser.add_argument('-ns', '--noswitch', dest='noswitch',
                        action='store_const', const=True,
                        help='don\'t switch after the first door is revealed')
    parser.add_argument('-n', '--tries', metavar='N', action='store',
                        dest='tries',
                        help='how many times to run the simulation')
    return p.parse_args()

###### MAIN ############

wins = 0
losses = 0
sw = True
n = 3000
parser = argparse.ArgumentParser(description='Simulates the Monty Hall Problem')
args = parse_args(parser)

if args.switch:
    sw = True
elif args.noswitch:
    sw = False
if args.tries:
    n = int(args.tries)

for i in range(n):
    ds = [ Door(True), Door(False), Door(False) ]
    if switch(pickadoor(ds), sw):
        wins += 1
    else:
        losses += 1
print("Wins: " + str(wins))
print("Losses: " + str(losses))
