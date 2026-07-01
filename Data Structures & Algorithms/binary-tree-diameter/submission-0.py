# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        self.diameter(root)
        return self.mx
        
    def diameter(self, node):
        if not node:
            return 0

        left, right = self.diameter(node.left), self.diameter(node.right)

        self.mx = max(self.mx, left+right)

        return 1 + max(left, right)
        