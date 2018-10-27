#!/usr/bin/env python3
import random
import argparse

def parse_args(p):
    """ parses command-line arguments and returns an arguments object """
    p.add_argument('choice', choices=['stay', 'switch'],
                   help='keep your initial choice or switch doors')
    p.add_argument('-t', '--tries', metavar='TRIES', action='store',
                   dest='tries', default=3000,
                   help='how many times to run the simulation (default 3000)')
    return p.parse_args()


parser = argparse.ArgumentParser(description='Simulates the Monty Hall Problem')
args = parse_args(parser)
initdoors = (True, False, False)
switch = True if args.choice == 'switch' else False
wins = 0

for i in range(int(args.tries)):
    initial = initdoors[random.randint(0, 2)]
    win = not initial if switch else initial
    if win:
        wins += 1
print('Wins:' + str(wins))
print('Losses:' + str(int(args.tries) - wins))
