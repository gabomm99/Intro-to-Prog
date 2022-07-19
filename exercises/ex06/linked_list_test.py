"""Tests for linked list utils."""


from exercises.ex06.linked_list import Node, last, value_at, max, linkify, scale, is_equal, concat, sub, splice

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty List should be the empty list."""
    assert last(None) is None


def test_last_empty_nonext() -> None:
    """Last of a list with just the head should return the head."""
    assert last(Node(2, None)) == 2


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Checks that value at any index of an empty list returns None."""
    assert value_at(None, 3) is None


def test_value_at_out_of_index() -> None:
    """Checks that a if an Index does not exist function returns None."""
    assert value_at(Node(2, None), 2) is None


def test_value_at_good_index() -> None:
    """Checks that a given linked list of 3 values returns the value at index 2 when asked."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max__empty_list() -> None:
    """Max should return None when list is empty."""
    assert max(None) is None


def test_max_one_value() -> None:
    """Max value of a list with one value is that value."""
    assert max(Node(2, None)) == 2


def test_max_value_of_linked_list() -> None:
    """Check that the max value of a list with three itemes, is the biggest value."""
    linked_list = Node(1, Node(3, Node(2, None)))
    assert max(linked_list) == 3


def test_linkify_empty_list() -> None:
    """Check if an empty list returns None."""
    assert linkify([]) is None


def test_linkify_one_item() -> None:
    """Check if a list of one item returns only that item."""
    node = Node(2, None)
    list = [2]
    assert is_equal(linkify(list), node)


def test_linkify_many_items() -> None:
    """Verify that a list with three items returns a linked list with those items in order."""
    node = Node(2, Node(1, Node(3, None)))
    assert is_equal(linkify([2, 1, 3]), node)


def test_scale_none() -> None:
    """Verify that scaling up an empty linked list returns None."""
    assert scale(None, 2) is None

 
def test_scale_factor_1() -> None:
    """Check that multiplying by 1 still creates a new list."""
    assert is_equal(scale(Node(1, Node(2, Node(3, None))), 1), Node(1, Node(2, Node(3, None))))


def test_scale_multy_list() -> None:
    """Verify that a list of three items is scaled up by two on each item."""
    assert is_equal(scale(Node(1, Node(2, Node(3, None))), 2), Node(2, Node(4, Node(6, None))))


def test_concat_two_empty() -> None:
    """Verify that when giving two None linked list, it returns None."""
    assert concat(None, None) is None


def test_concat_lhs_empty() -> None:
    """Verify that when lhs is None, the result list is rhs only."""
    lhs = None
    rhs = linkify([4, 5, 6])
    node = Node(4, Node(5, Node(6, None)))
    assert is_equal(node, concat(lhs, rhs))


def test_concat_rhs_empty() -> None:
    """Verify that when rhs is None, the result list is lhs only."""
    rhs = None
    lhs = linkify([4, 5, 6])
    node = Node(4, Node(5, Node(6, None)))
    assert is_equal(node, concat(lhs, rhs))


def test_concat_two_linked_list() -> None:
    """Verify that when both rhs and lhs are actual list the result is a Node with lhs followed by rhs."""
    lhs = linkify([1, 2, 3])
    rhs = linkify([4, 5, 6])
    node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
    assert is_equal(node, concat(lhs, rhs))


def test_sub_empty_list() -> None:
    """Checks if sub returns None when list is empty."""
    sub(None, 2, 3) is None


def test_sub_start_below_0() -> None:
    """Checks if the sub list starts from index zero even when start is less than zero."""
    list = linkify([1, 2, 3, 4])
    node = Node(1, Node(2, Node(3, None)))
    assert is_equal(node, sub(list, -1, 3))


def test_sub_in_range() -> None:
    """Verify that when both rhs and lhs are actual list the result is a Node with lhs followed by rhs."""
    list = linkify([1, 2, 3])
    node = Node(2, Node(3, None))
    assert is_equal(node, sub(list, 1, 2))


def test_sub_larger_start() -> None:
    """Checks what happens when start is bigger than length of link list."""
    list = linkify([1, 2, 3])
    assert sub(list, 8, 3) is None


def test_sub_larger_length_than_actual() -> None:
    """Verifies that sub returns the list up to the end when given length larger than original list."""
    list = linkify([1, 2, 3])
    node = Node(1, Node(2, Node(3, None)))
    assert is_equal(node, sub(list, 0, 5))


def test_splice_both_lists_empty() -> None:
    """Checks that when both list are is empty this function returns none."""
    assert splice(None, 1, None) is None


def test_splice_index_less_zero() -> None:
    """Checks that list_b attaches before index zero when given index is less than zero."""
    list = linkify([1, 2, 3])
    list_b = linkify([4, 5, 6])
    node = linkify([4, 5, 6, 1, 2, 3])
    assert is_equal(node, splice(list, -2, list_b))


def test_splice_index_too_big() -> None:
    """Verifies that list_b attaches at the end when index is bigger than length of list_a."""
    list = linkify([1, 2, 3])
    list_b = linkify([4, 5, 6])
    node = linkify([1, 2, 3, 4, 5, 6])
    assert is_equal(node, splice(list, 4, list_b))