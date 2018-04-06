# Program simulating a 'random walk' probabilistic simulation
from random import *

def main():

    intro()
    n = int(input("How many coin tosses would you like to take? \n"
    "Enter a number: "))
    total = steps(n)
    printSummary(total, n)

def intro():
    print()
    print("Welcome to the 'random walk' simulator!")
    print()
    print("This program will simulate coin tosses to decide  \n"
    "how far away you will end up from a starting point. Each heads \n"
    "has you take one step forward, while each tails has you take \n"
    "one step back.")


def steps(i):
    tosses = 0
    total_steps = 0
    while (tosses < i):
        total_steps, tosses = oneStep(total_steps, tosses)

    return total_steps


def oneStep(step, toss):
    if random() < 0.5:
        step = step + 1
    else:
        step = step - 1

    toss = toss + 1

    return step, toss

def printSummary(steps, j):
    if steps > 0:
        print("After " + str(j) + " tosses, you have wound up " + str(steps) + "\n"
        "steps forward from your starting point.")

    elif steps < 0:
        print("After " + str(j) + " tosses, you have wound up " + str(abs(steps)) + "\n"
        "steps back from your starting point.")

    else:
        print("After " + str(j) + " tosses, you have wound up right where you started.")



if __name__ == '__main__': main()
