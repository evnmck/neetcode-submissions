# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root,0)
    
    def depth(self, node, i):
        if not node:
            return i

        return max(self.depth(node.left, i + 1), self.depth(node.right, i + 1))
        