"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        return self.cloneNode(root)

    def cloneNode(self, node: 'Node') -> 'Node':
        new_children = []
        for child in node.children:
            new_children.append(self.cloneNode(child))
        new_node = Node(node.val, new_children)
        return new_node
