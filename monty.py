#!/usr/bin/env python3
import random
import argparse

###### DEFINITIONS ############

# the doors could just be booleans but for now this preserves uniqueness
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

# doors is a tuple (initial choice, other door), switchornot is a boolean
# returns true if the chosen door is a winner
def switch(doors, switchornot):
    if switchornot:
        return doors[1].isitawin()
    else:
        return doors[0].isitawin()

# command-line args
def parse_args(p):
    parser.add_argument('--switch', '-s', dest='switch', action='store_const',
                        const=True,
                        help='switch after the first door is revealed')
    parser.add_argument('--noswitch', 'ns', dest='noswitch',
                        action='store_const', const=True,
                        help='don\'t switch after the first door is revealed')
    parser.add_argument('-n', '--tries', metavar='N', action='store',
                        default=3000, dest='tries',
                        help='how many times to run the simulation\
                        (default 3000)')
    return p.parse_args()

###### MAIN ############

wins = 0
losses = 0
switchornot = True
parser = argparse.ArgumentParser(description='Simulates the Monty Hall Problem')
args = parse_args(parser)

if args.switch:
    switchornot = True
elif args.noswitch:
    switchornot = False

for _ in range(int(args.tries)):
    ds = [ Door(True), Door(False), Door(False) ]
    if switch(pickadoor(ds), switchornot):
        wins += 1
    else:
        losses += 1

print("Wins: " + str(wins))
print("Losses: " + str(losses))
