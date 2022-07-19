"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional, List

__author__ = "Your PID"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> Optional[int]:
    """Returns the last value of a Linked List, or None if the list is empty."""
    if head is None:
        return None
    elif head.next is None:
        return head.data
    else:
        return last(head.next)
    

def includes(hystack: Optional[Node], needle: int) -> bool:
    """Is needle in the haystack."""
    if hystack is None:
        return False
    elif hystack.data == needle:
        return True
    else:
        return includes(hystack.next, needle)


def seq(lo: int, hi: int) -> Optional[Node]:
    """A function that makes a linked list from lo to high."""
    if lo >= hi:
        return None
    else:
        return Node(lo, seq(lo + 1, hi))


def value_at(head: Optional[Node], index: int) -> Optional[int]:
    """A function that looks for the value at the giving index, if it exists."""
    if head is None:
        return None
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)

    
def max(head: Optional[Node]) -> Optional[int]:
    """A function that finds the maximum value of a linked list."""
    if head is None:
        return None
    else:
        next_val = max(head.next)
        if next_val is None:
            return head.data
        elif next_val > head.data:
            return next_val
        else:
            return head.data
    

def linkify(items: List[int]) -> Optional[Node]:
    """A function that 'transforms' a List of type List to a linked list of Class Node."""
    if items == []:
        return None
    else:
        node = Node(items[0], linkify(items[1:]))
        return node


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """A function that multiplies each element of a linked list by a x factor."""
    if head is None:
        return None
    else:
        new_node = head.data * factor
        return Node(new_node, scale(head.next, factor))


def concat(lhs: Optional[Node], rhs: Optional[Node]) -> Optional[Node]:
    """A function that concatenates two separate linked lists."""
    if rhs is None and lhs is None:
        return None
    elif lhs is None:
        if rhs is not None:
            new_node = Node(rhs.data, concat(None, rhs.next))
            return new_node
    else: 
        new_node = Node(lhs.data, concat(lhs.next, rhs))
        return new_node
    

def sub(list: Optional[Node], start: int, length: int) -> Optional[Node]:
    """A function that creates a sublist from the given index and with the given length."""
    if list is None or length == 0:
        return None
    elif start > 0:
        return sub(list.next, start - 1, length)
    else:
        return Node(list.data, sub(list.next, start, length - 1))
        

def splice(list_a: Optional[Node], index: int, list_b: Optional[Node]) -> Optional[Node]:
    """A function that inserts one linked list into another at the given index."""
    if list_a is None and index != 0:
        if list_b is not None:
            return Node(list_b.data, list_b.next)
    if list_a is None and list_b is not None:
        return Node(list_b.data, list_b.next)
    if list_a is None:
        return None
    if list_b is None:
        return Node(list_a.data, list_a.next)
    elif index > 0:
        return Node(list_a.data, splice(list_a.next, index - 1, list_b))
    else:
        return Node(list_b.data, splice(list_a, index, list_b.next))
