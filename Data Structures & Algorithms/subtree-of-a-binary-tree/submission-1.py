# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.recursive(root, subRoot)

    def recursive(self, node1, node2):
        
        if not node1:
            return False
            
        isSub = self.sub(node1, node2)

        if isSub:
            return True
        
        return self.recursive(node1.left, node2) or self.recursive(node1.right, node2)

    def sub(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.sub(node1.left, node2.left) and self.sub(node1.right, node2.right)
        
        