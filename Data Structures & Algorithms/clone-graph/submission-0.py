"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        queue = deque()
        nodes = {}

        queue.append(node)
        nodes[node] = Node(node.val)

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                nodes[curr_node].neighbors.append(nodes[neighbor])
                    
        return nodes[node]

