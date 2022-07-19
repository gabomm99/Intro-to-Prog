"""Example of a constructur definition."""

class Point:
    """A 2D point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """An example of a constructur function/method."""
        self.x = x
        self.y = y


def main() -> None:
    """The entrypoint."""
    p = Point(110.0, 211.0)
    print(p.x)
    print(p.y)


if __name__ == "__main__":
    main()