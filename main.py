from typing import Self


class Node:
    def __init__(self, key: int):
        self.left: Self = None
        self.right: Self = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root: Node | None, key: int) -> Node:
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def search(root: Node | None, key: int) -> Node | None:
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def delete(root: Node | None, key: int):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = tree_min_value(root.right)
        root.right = delete(root.right, root.val)
    return root


# Завдання 1
def tree_min_value(root: Node) -> int:
    current = root
    while current.left is not None:
        current = current.left
    return current.val


# Завдання 2
def tree_max_value(root: Node) -> int:
    current = root
    while current.right is not None:
        current = current.right
    return current.val


# Завдання 3
def tree_sum(root: Node) -> int:
    sum = root.val
    if root.left:
        sum += tree_sum(root.left)
    if root.right:
        sum += tree_sum(root.right)
    return sum


if __name__ == '__main__':
    # Test
    tree = Node(5)
    tree = insert(tree, 3)
    tree = insert(tree, 2)
    tree = insert(tree, 4)
    tree = insert(tree, 7)
    tree = insert(tree, 6)
    tree = insert(tree, 8)

    print(tree)

    print('Min: ', tree_min_value(tree))
    print('Max: ', tree_max_value(tree))
    print('Sum: ', tree_sum(tree))
