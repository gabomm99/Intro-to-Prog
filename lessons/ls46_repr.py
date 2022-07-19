"""Demo of __repr__ magic method."""

from typing import List, Dict
class Point:
    x: float = 0.0
    y: float = 0.0

    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return f"({self.x}, {self.y})"


p0: Point = Point()
p0.x = 1.0
print(p0)

list: List[str] = ["hi", "bye", "done", "tont", "pill"]
dicto: Dict[str, int] = {"hi" : 2, "bye" : 3, "chao" : 4}
last: str = list.pop(len(list) - 1)
print(last)