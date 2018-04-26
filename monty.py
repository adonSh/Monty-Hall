#!/usr/bin/env python3
import random
import argparse

###### DEFINITIONS ############

# selects a door at random, removes a losing door, and
# returns a tuple containing the choice and the remaining door
def pickadoor(doors):
    guess = random.randint(0, 2)
    door = doors[guess]

    return (door, not door)

# doors is a tuple (initial choice, other door), switchornot is a boolean
# returns true if the chosen door is a winner
def switchornot(doors, switch):
    return doors[1] if switch else doors[0]

# process command-line args
# returns arguments object
def parse_args(p):
    p.add_argument('choice', choices=['stay', 'switch'],
                   help='keep your initial choice or switch doors')
    p.add_argument('-t', '--tries', metavar='TRIES', action='store',
                        default=3000, dest='tries',
                        help='how many times to run the simulation\
                        (default 3000)')
    p.add_argument('-n', '--doors', metavar='DOORS', action='store',
                   default=3, dest='doors',
                   help='how many doors to use in the simulation (default 3)')
    return p.parse_args()

###### MAIN ############
# TODO: implement n-doors

wins = 0
losses = 0
parser = argparse.ArgumentParser(description='Simulates the Monty Hall Problem')
args = parse_args(parser)
switch = True if args.choice == 'switch' else False

for _ in range(int(args.tries)):
    doors = (True, False, False)
    if switchornot(pickadoor(doors), switch):
        wins += 1
    else:
        losses += 1

print('Wins: ' + str(wins))
print('Losses: ' + str(losses))
