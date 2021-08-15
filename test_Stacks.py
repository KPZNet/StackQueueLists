from Stacks import StackList
from Stacks import StackLinkedList

def test_is_empty_list():
    stk = StackList()
    stk.push(1)
    stk.push(3)
    stk.pop()
    stk.pop()
    assert stk.isEmpty()


def test_push_list():
    stk = StackList()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    r = stk.pop()
    assert r == 3


def test_pop_list():
    stk = StackList()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.pop()
    stk.pop()
    r = stk.pop()
    assert r == 1

def test_is_empty_linkedlist():
    stk = StackLinkedList()
    stk.push(1)
    stk.push(3)
    stk.pop()
    stk.pop()
    assert stk.isEmpty()


def test_push_linkedlist():
    stk = StackLinkedList()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    r = stk.pop()
    assert r == 3


def test_pop_linkedlist():
    stk = StackLinkedList()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.pop()
    stk.pop()
    r = stk.pop()
    assert r == 1

test_push_list()
test_pop_list()
test_is_empty_list()

test_push_linkedlist()
test_pop_linkedlist()
test_is_empty_linkedlist()