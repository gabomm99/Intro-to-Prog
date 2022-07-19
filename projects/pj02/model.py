"""The model classes maintain the state and logic of the simulation."""


from __future__ import annotations


__author__ = "730442926"


from typing import List
from random import random
import constants
from math import sin, cos, pi, sqrt


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, point_b: Point) -> float:
        """A method that find the distance between two points."""
        inside_part: float = ((point_b.x - self.x)**2) + ((point_b.y - self.y)**2)
        dist: float = sqrt(inside_part)
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassigns objects location when called upon."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Assigns the the value of INFECTED to attribute sickness."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """A method that changes sickness status to IMMUNE."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Check point for sickness status of the sickness attribute."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
        
    def is_infected(self) -> bool:
        """Check point for sickness status of the sickness attribute."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
 
    def is_immune(self) -> bool:
        """Checkpoint for immunization of an individual."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def contact_with(self, other: Cell) -> None:
        """Checkpoint for contact between infected and uninfected individuals."""
        if self.is_infected():
            if other.is_vulnerable():
                other.contract_disease()
                other.color()
        if other.is_infected():
            if self.is_vulnerable():
                self.contract_disease()
                self.color()
   
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "blue"
        elif self.is_immune():
            return "orange"
        else:
            return "black"

   
class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells:
            raise ValueError(f"Initial infected people cannot be more than {cells}")
        if infected <= 0:
            raise ValueError("At least 1 initial person must be infected")
        if (infected + immune) >= cells:
            raise ValueError(f"Initial infected plus immunes people cannot be more than {cells}")
        if immune >= cells:
            raise ValueError(f"Initial immune people cannot be more than {cells}")
        if immune < 0:
            raise ValueError("Initial immune people cannot be less than zero")
        for _ in range(0, cells):
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            self.population.append(Cell(start_loc, start_dir))
        for i in range(0, infected):
            self.population[i].contract_disease()
        for i in range(infected, infected + immune):
            self.population[i].immunize()
             
    def check_contacts(self) -> None:
        """Checks for contact between people."""
        for i in range(0, len(self.population)):
            for j in range(0, len(self.population)):
                if j < i:
                    if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                        self.population[i].contact_with(self.population[j])
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        tracker: int = 0
        for cell in self.population:
            if cell.is_infected() is False:
                tracker += 1
            if tracker == len(self.population):
                return True
        return False