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
            newhead = Node(value)
            newhead.next = self.head
            self.head = newhead
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
        newnode = Node(value)
        newnode.next = after.next
        after.next = newnode
    def pop(self) -> Any:
        prevhead = self.head
        newhead = self.head.next
        del(self.head)
        self.head = newhead
        return prevhead
    def remove_last(self) -> Any:
        prevtail = self.tail
        newtail = self.head
        while 1:
            node1 = newtail.next
            if node1 == self.tail:
                break
            newtail = node1
        newtail.next = None
        del(self.tail)
        self.tail = newtail
        return node1
    def remove(self, after: Node) -> Any:
        removed = after.next
        after.next = removed.next
        del(removed)
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
        len = 0
        if self.head is not None:
            head = self.head
            len += 1
            while 1:
                len += 1
                head = head.next
                if head.next is None:
                    break
        return len

list = LinkedList()
list.push(1)
list.push(0)
assert str(list) == '0 -> 1'
list.append(9)
list.append(10)
assert str(list) == '0 -> 1 -> 9 -> 10'
middle_node = list.node(at=1)
list.insert(5, after=middle_node)
assert str(list) == '0 -> 1 -> 5 -> 9 -> 10'
first_element = list.node(at=0)
returned_first_element = list.pop()
assert first_element == returned_first_element
last_element = list.node(at=3)
returned_last_element = list.remove_last()
assert last_element == returned_last_element
assert str(list) == '1 -> 5 -> 9'
second_node = list.node(at=1)
list.remove(second_node)
assert str(list) == '1 -> 5'
print(len(list))
print('List: ', list)


