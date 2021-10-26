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


class Stack:
    storage: LinkedList

    def __init__(self):
        self.storage = None

    def push(self, elements: Any) -> None:
        if self.storage is None:
            self.storage = LinkedList()
            self.storage.push(elements)
        else:
            self.storage.push(elements)

    def pop(self) -> Any:
        node = self.storage.pop()
        return node.value

    def __str__(self) -> str:
        string: str = ''
        if self.storage is not None:
            node = self.storage.head
            while 1:
                string = string + str(node.value) + '\n'
                if node.next is None:
                    break
                node = node.next
            return string

    def __len__(self):
        length = 0
        if self.storage is not None:
            pile = self.storage.head
            while 1:
                length += 1
                if pile.next is None:
                    break
                pile = pile.next
        return length


stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2
