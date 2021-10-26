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


class Queue:
    storage: LinkedList

    def __init__(self):
        self.storage = None

    def peek(self) -> Any:
        return self.storage.tail

    def enqueue(self, element: Any) -> None:
        if self.storage is None:
            self.storage = LinkedList()
            self.storage.append(element)
        else:
            self.storage.append(element)

    def dequeue(self) -> Any:
        last = self.storage.pop()
        return last.value

    def __str__(self):
        string: str = ''
        if self.storage is not None:
            data = self.storage.head
            while data is not None:
                string = string + str(data.value) + ', '
                data = data.next
                if data.next is None:
                    string = string + str(data.value)
                    break
        return string

    def __len__(self):
        length = 0
        linked_list = self.storage
        if linked_list is not None:
            length += 1
            while 1:
                linked_list_head = linked_list.head.next
                if linked_list_head.next is None:
                    length += 1
                    break
                length += 1

        return length


queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
client_first = queue.dequeue()
assert client_first == "klient1"
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
