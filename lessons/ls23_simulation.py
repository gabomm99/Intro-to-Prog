"""Stochastic example number 1!"""


from typing import List
from random import randint
from matplotlib import pyplot

TRIALS: int = 100
MAX_ROLL: int = 12


def main() -> None:
    """Entry point of simulator."""
    results: List[int] = simulate(TRIALS)

    counts: List[int] = count(results)

    plot(counts)


def simulate(n: int) -> List[int]:
    """Roll a pair of dice n times and return list of summed rolls."""
    rolls: List[int] = []
    # Loop n times and for each iteration:
    for trial in range(0, n):
        # 1. Roll a pir die
        roll: int = randint(1, 6) + randint(1, 6)
        # 2. Keep track of the results
        rolls.append(roll)
    return rolls


def count(results: List[int]) -> List[int]:
    tallies: List[int] = []
    for i in range(0, MAX_ROLL + 1):
        tallies.append(0)
    for result in results: 
        tallies[result] = tallies[result] + 1

    return tallies


def plot(counts: List[int]) -> None:
    """Plot the results of our simulated experiment in histograms"""
    pyplot.title("Distribution of Rolled Values")
    pyplot.xlabel("Sum of Roll")
    pyplot.ylabel("Frequency")
    xaxis_values: range = range(0, MAX_ROLL + 1)
    pyplot.bar(xaxis_values, counts)
    pyplot.show()




if __name__ == "__main__":
    main()



