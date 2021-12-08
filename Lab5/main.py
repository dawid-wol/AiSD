from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child and self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        _str = str(self.value)
        return _str

    def show(self, visit: Callable[[Any], None]):
        if self.right_child is not None:
            print(end='    ')
            self.right_child.show(visit)
        print(end='    ')
        print(self.value)
        print(end='    ')
        if self.left_child is not None:
            print(end='    ')
            self.left_child.show(visit)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.root.left_child is not None:
            self.root.left_child.traverse_in_order(visit)
        visit(self.root)
        if self.root.right_child is not None:
            self.root.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.root.left_child is not None:
            self.root.left_child.traverse_post_order(visit)
        if self.root.right_child is not None:
            self.root.right_child.traverse_post_order(visit)
        visit(self.root)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self.root)
        if self.root.left_child is not None:
            self.root.left_child.traverse_pre_order(visit)
        if self.root.right_child is not None:
            self.root.right_child.traverse_pre_order(visit)

    def show(self, visit: Callable[[Any], None]):
        if self.root.right_child is not None:
            print(end='    ')
            self.root.right_child.show(visit)
        print(self.root.value)
        if self.root.left_child is not None:
            print(end="    ")
            self.root.left_child.show(visit)


def _print(node: BinaryNode):
    print(node.value)


def get_level(node: BinaryNode, value, level):
    if node is None:
        return 0

    if node.value == value:
        return level
    down_level = get_level(node.left_child, value, level+1)

    if down_level != 0:
        return down_level
    down_level = get_level(node.right_child, value, level+1)

    return down_level


def check_level(_tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode):
    first_node_level = get_level(_tree.root, first_node.value, 1)
    second_node_level = get_level(_tree.root, second_node.value, 1)
    if first_node_level == second_node_level:
        return True
    else:
        return False


tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.add_right_child(2)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)

tree.show(tree)

print(check_level(tree, tree.root.left_child, tree.root.right_child))
