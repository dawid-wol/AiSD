from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head

    def append(self, value: Any) -> None:
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def node(self, at: int) -> Node:
        node1 = self.head
        for i in range(at):
            node1 = node1.next
        return node1

    def insert(self, value: Any, after: Node) -> None:
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def pop(self) -> Any:
        previous_head = self.head
        new_head = self.head.next
        self.head = new_head
        return previous_head

    def remove_last(self) -> Any:
        new_tail = self.head
        while 1:
            node1 = new_tail.next
            if node1 == self.tail:
                break
            new_tail = node1
        new_tail.next = None
        self.tail = new_tail
        return node1

    def remove(self, after: Node) -> Any:
        removed = after.next
        after.next = removed.next

    def __str__(self) -> str:
        string: str = ''
        data = self.head
        while data is not None:
            string = string + str(data.value)
            data = data.next
            if data is not None:
                string = string + ' -> '
        return string

    def __len__(self):
        length = 0
        if self.head is not None:
            head = self.head
            length += 1
            while 1:
                length += 1
                head = head.next
                if head.next is None:
                    break
        return length


_list = LinkedList()
_list.push(1)
_list.push(0)
assert str(_list) == '0 -> 1'
_list.append(9)
_list.append(10)
assert str(_list) == '0 -> 1 -> 9 -> 10'
middle_node = _list.node(at=1)
_list.insert(5, after=middle_node)
assert str(_list) == '0 -> 1 -> 5 -> 9 -> 10'
first_element = _list.node(at=0)
returned_first_element = _list.pop()
assert first_element == returned_first_element
last_element = _list.node(at=3)
returned_last_element = _list.remove_last()
assert last_element == returned_last_element
assert str(_list) == '1 -> 5 -> 9'
second_node = _list.node(at=1)
_list.remove(second_node)
assert str(_list) == '1 -> 5'
