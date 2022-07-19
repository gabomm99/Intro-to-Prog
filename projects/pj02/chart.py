"""Simulation of virus contagiousness and its immunization and infection curve.

Hypothetical scenario presented: If 10 infected people came into my town, Graham NC, out of the 15806 residents,
about 80% of them would contract the virus, and eventually recovered (everybody recovers in this modele). 
Note: For practical matters, the population is scaled down by a factor of 100,
leaving my modele with a population of about 151 people. Also, I have extended the bounderies as much as possible,
to represent the maximum area of the town of Graham.
Result: My hypothesis was fairly accurate. The graph attached to this directory shows how approximately 79.5%
of the population contracted the virus throughout the course of the simulation. Only about 21 people did not 
get infected, which only represents about 20.5% of Graham's population scaled down by 100.
"""


import sys
from typing import Dict, List
from projects.pj02.model import constants, Model


def main() -> None:
    """Entry point of simulation for virus."""
    args: Dict[str, str] = check_args()
    model: Model = Model(int(args["num_cells"]), constants.CELL_SPEED, int(args["num_infected"]), int(args["num_immune"]))
    infected_tracker: List[int] = []
    immune_tracker: List[int] = []
    tick_tracker: List[int] = []
    tick_count: int = 0
    while model.is_complete() == False:  
        model.tick()
        tick_count += 1
        tick_tracker.append(tick_count)
        count_in: int = 0
        count_immu: int = 0
        for cell in model.population:
            if cell.is_infected():
                count_in += 1
            if cell.is_immune():
                count_immu += 1
        infected_tracker.append(count_in)
        immune_tracker.append(count_immu)
    line_chart_data(tick_tracker, infected_tracker, immune_tracker)
    
    
def line_chart_data(simulation_times: List[int], infected_cells: List[int], immune_cells: List[int]) -> None:
    """A function that edits a list of dates and times plots a scatter plot of all the SOD!
    
    atmospheric data under a specific column!
    """
    import matplotlib.pyplot as plt
    plt.plot(simulation_times, infected_cells)
    plt.plot(simulation_times, immune_cells)
    plt.xticks(fontsize=10)
    plt.xlabel("Simluation Periods")
    plt.ylabel("Infected Cells, Immune Cells")
    plt.title("Projection of Contagion in Graham NC")
    plt.show()


def check_args() -> Dict[str, str]:
    """Check for valid arguments and return in Dictionary with CLI arguments and keys for each of them."""
    if len(sys.argv) != 4:
        print(f"Usage: python -m projects.pj02.chart [Number of people] [Initial infected people] [Immunized Poeple]")
        exit()
    return {
        "num_cells": sys.argv[1],
        "num_infected": sys.argv[2],
        "num_immune": sys.argv[3]
    }

















if __name__ == "__main__":
    main()