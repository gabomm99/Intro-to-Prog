"""Demonstration of a recursive data structure!"""

from __future__ import annotations
from typing import Optional


class Node:
    data: int = 0
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next


def count(a_node: Optional[Node]) -> int:
    if a_node == None:
        return 0
    else:
        return 1 + count(a_node.next)



head: Node = Node(210, None)
head = Node(110, head)


